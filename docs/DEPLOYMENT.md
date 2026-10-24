# 🚀 Deployment Guide

This guide covers all supported ways to deploy ATLAS — from a quick local setup to a production cloud environment.

---

## Table of Contents

- [Option 1: Docker Compose (Recommended)](#option-1-docker-compose-recommended)
- [Option 2: Manual / Local Development](#option-2-manual--local-development)
- [Option 3: Cloud Deployment](#option-3-cloud-deployment)
- [Production Checklist](#production-checklist)
- [Health Checks](#health-checks)
- [Logs & Monitoring](#logs--monitoring)
- [Updating ATLAS](#updating-atlas)
- [Troubleshooting](#troubleshooting)

---

## Option 1: Docker Compose (Recommended)

The fastest way to run the full ATLAS stack.

### Prerequisites

| Tool | Minimum Version | Check |
|------|----------------|-------|
| Docker | 24.0 | `docker --version` |
| Docker Compose | 2.20 | `docker compose version` |
| Git | 2.30 | `git --version` |
| RAM | 4 GB free | — |
| Disk | 5 GB free | — |

### Step-by-step

**1. Clone the repository (with all submodules)**

```bash
git clone --recurse-submodules https://github.com/cepdnaclk/e22-co2060-hydro-risk-management.git
cd e22-co2060-hydro-risk-management
```

> If you already cloned without submodules:
> ```bash
> git submodule update --init --recursive
> ```

**2. Set up environment variables**

```bash
cp .env.example .env
```

Open `.env` in a text editor and update at minimum:
- `POSTGRES_PASSWORD` — use a strong password
- `JWT_SECRET` — generate one: `openssl rand -hex 32`
- `ADMIN_PASSWORD` — change from the default `admin123`

**3. Build and start all services**

```bash
docker compose up --build -d
```

This starts **9 containers**. First boot takes **3–5 minutes** while:
- TimescaleDB initializes and creates the `kernelx` database
- Spring Boot services wait for the DB to be ready
- Maven builds the JARs inside Docker (if no cache)

**4. Check all services are running**

```bash
docker compose ps
```

Expected output:
```
NAME                         STATUS          PORTS
master_timescaledb           running         0.0.0.0:5432->5432/tcp
redis_cache                  running         0.0.0.0:6379->6379/tcp
metadata-handling-service    running         0.0.0.0:8092->8092/tcp
alerting-service             running         0.0.0.0:8093->8093/tcp
mqtt-subscriber-service      running         0.0.0.0:8091->8091/tcp
report-generating-service    running         0.0.0.0:8094->8094/tcp
user-service                 running         0.0.0.0:8096->8096/tcp
gis-monitoring-service       running         0.0.0.0:8097->8097/tcp
frontend                     running         0.0.0.0:8090->80/tcp
```

**5. Access the application**

| URL | Description |
|-----|-------------|
| http://localhost:8090 | 🌐 Main Dashboard (login: admin / admin123) |
| http://localhost:8092/swagger-ui.html | 📋 Metadata API docs |
| http://localhost:8096/swagger-ui.html | 👤 Auth API docs |

---

## Option 2: Manual / Local Development

Use this approach when developing or modifying ATLAS services.

### Start the database and Redis only

```bash
docker compose up db redis -d
```

### Run each service manually

**Backend service (example: alerting service)**
```bash
cd disaster-management-alerting-service

# Using Maven wrapper (recommended)
./mvnw spring-boot:run

# On Windows
mvnw.cmd spring-boot:run
```

Make sure each service's `application.yml` points to `localhost:5432` (not `db:5432`).

**Frontend**
```bash
cd disaster-management-frontend
npm install
npm run dev
# Runs at http://localhost:5173
```

### Service startup order (for manual setup)

```
1. db (TimescaleDB)     ← Start first, wait ~30s
2. redis               ← Start second
3. user-service        ← Required by other services for JWT validation
4. metadata-service    ← Core entity data
5. mqtt-service        ← Starts ingesting data immediately
6. alerting-service    ← Reads sensor data, generates alerts
7. gis-service         ← Reads sensors + alerts for map
8. report-service      ← Reads historical data
9. frontend            ← Calls all backend services
```

---

## Option 3: Cloud Deployment

### AWS (EC2 + RDS)

**Architecture:**

```
Internet → ALB → EC2 (Docker Services)
                      → RDS (PostgreSQL + TimescaleDB extension)
                      → ElastiCache (Redis)
```

**Steps:**

1. **Provision RDS** — Use `PostgreSQL 14` engine. Enable TimescaleDB extension:
   ```sql
   CREATE EXTENSION IF NOT EXISTS timescaledb;
   ```

2. **Provision ElastiCache** — Redis cluster, single node is sufficient for token blacklisting.

3. **Set environment variables** on EC2:
   ```bash
   export SPRING_DATASOURCE_URL=jdbc:postgresql://your-rds-endpoint:5432/kernelx
   export SPRING_DATA_REDIS_HOST=your-elasticache-endpoint
   ```

4. **Deploy with Docker Compose** on EC2 (comment out `db` and `redis` services, they're now managed):
   ```bash
   docker compose up --build -d \
     metadata-handling-service \
     alerting-service \
     mqtt-service \
     report-generating-service \
     user-service \
     gis-monitoring-service \
     frontend
   ```

5. **Configure ALB** to route traffic to port 8090 (or add Nginx in front).

### Google Cloud (GKE)

A Kubernetes deployment guide is available as a community contribution. See [discussions](https://github.com/cepdnaclk/e22-co2060-hydro-risk-management/discussions).

### Docker Swarm

```bash
# Initialize swarm
docker swarm init

# Deploy the stack
docker stack deploy -c docker-compose.yml atlas
```

---

## Production Checklist

Before going live, work through this checklist:

### Security
- [ ] Changed `ADMIN_PASSWORD` from `admin123` to a strong password
- [ ] Generated a new `JWT_SECRET` (`openssl rand -hex 32`)
- [ ] Changed `POSTGRES_PASSWORD` to a strong value
- [ ] Switched to a **private MQTT broker** (not public HiveMQ)
- [ ] Enabled **TLS** on MQTT (`ssl://` instead of `tcp://`)
- [ ] Configured MQTT authentication (username/password or certificates)
- [ ] Enabled HTTPS on the frontend (SSL certificate via Let's Encrypt or ALB)
- [ ] Removed or restricted Swagger UI endpoints (`springdoc.swagger-ui.enabled=false`)

### Database
- [ ] Enabled **automated backups** for TimescaleDB
- [ ] Changed `spring.jpa.hibernate.ddl-auto` from `update` to `validate` in all services
- [ ] Set up **TimescaleDB retention policies** for old sensor readings
- [ ] Configured database **connection pooling** (HikariCP settings)

### Infrastructure
- [ ] Set up **log aggregation** (ELK, CloudWatch, Grafana Loki)
- [ ] Configured **health check endpoints** for load balancer
- [ ] Enabled **Docker restart policies** (`restart: unless-stopped`)
- [ ] Set resource limits on containers (CPU/RAM)

### Monitoring
- [ ] Set up alerts for service health (e.g., PagerDuty, Uptime Robot)
- [ ] Configured Prometheus + Grafana for metrics (optional)

---

## Health Checks

Each Spring Boot service exposes Spring Actuator health endpoints:

```bash
# Check a service health
curl http://localhost:8092/actuator/health

# Expected response when healthy
{"status":"UP","components":{"db":{"status":"UP"},"redis":{"status":"UP"}}}
```

**Quick health check for all services:**
```bash
for port in 8091 8092 8093 8094 8096 8097; do
  echo -n "Service :$port — "
  curl -s http://localhost:$port/actuator/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('status','UNKNOWN'))"
done
```

---

## Logs & Monitoring

### View logs via Docker Compose

```bash
# All services
docker compose logs -f

# Specific service (follow)
docker compose logs -f alerting-service

# Last 100 lines of user service
docker compose logs --tail=100 user-service
```

### Log format

All Spring Boot services use `Logback` with structured logging. Key log levels:

| Level | Meaning |
|-------|---------|
| `INFO` | Normal operation, scheduled job results |
| `WARN` | Data validation failures, non-critical issues |
| `ERROR` | Exceptions, DB connection failures |
| `DEBUG` | Detailed request/response (disabled in production) |

---

## Updating ATLAS

### Update submodules to their latest commits

```bash
git submodule update --remote --merge
git add .
git commit -m "chore: update all submodules to latest"
```

### Rebuild and restart changed services

```bash
# Rebuild all (safe, preserves volumes)
docker compose up --build -d

# Rebuild a specific service only
docker compose up --build -d alerting-service
```

---

## Troubleshooting

### Services fail to start (DB not ready)

Spring Boot services may start before TimescaleDB finishes initializing. Wait 30–60 seconds and run:
```bash
docker compose restart metadata-handling-service alerting-service
```

Or, to avoid this, add health checks to `docker-compose.yml`:
```yaml
depends_on:
  db:
    condition: service_healthy
```

### MQTT not receiving data

1. Check the broker and topic are correct in `application.yml`
2. Check the MQTT service logs: `docker compose logs mqtt-subscriber-service`
3. Use [MQTT Explorer](https://mqtt-explorer.com/) to verify your device is publishing
4. Verify the topic pattern — `thw/telemetry/#` uses wildcard `#` for any sub-topic

### Frontend cannot reach backend services

The frontend uses Nginx as a reverse proxy. Check `disaster-management-frontend/nginx.conf` to ensure proxy_pass URLs are correct for your environment.

### Port conflicts

If any port is already in use, edit the left side of the port mapping in `docker-compose.yml`:
```yaml
ports:
  - "18092:8092"  # Use 18092 on host if 8092 is taken
```

### Database connection refused

```bash
# Check if TimescaleDB is running
docker compose ps db

# Connect to DB manually to verify
docker exec -it master_timescaledb psql -U kernelx -d kernelx

# Check if tables exist
\dt
```
