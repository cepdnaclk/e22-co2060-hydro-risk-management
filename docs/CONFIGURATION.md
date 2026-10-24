# ⚙️ Configuration Reference

Every configurable aspect of ATLAS, organized by service.

---

## Environment Variables (`.env` file)

Copy `.env.example` to `.env` and set these values before starting with Docker Compose.

### Database

| Variable | Default | Description |
|----------|---------|-------------|
| `POSTGRES_DB` | `kernelx` | Database name |
| `POSTGRES_USER` | `kernelx` | Database username |
| `POSTGRES_PASSWORD` | *(required)* | Database password — **change from default!** |

### JWT / Authentication

| Variable | Default | Description |
|----------|---------|-------------|
| `JWT_SECRET` | *(required)* | 256-bit hex string for signing JWTs. Generate: `openssl rand -hex 32` |
| `JWT_EXPIRATION` | `900000` | Access token TTL in milliseconds (default: 15 minutes) |
| `JWT_REFRESH_EXPIRATION` | `86400000` | Refresh token TTL in milliseconds (default: 1 day) |

### Redis

| Variable | Default | Description |
|----------|---------|-------------|
| `REDIS_HOST` | `redis` | Redis hostname (use `redis` for Docker, `localhost` for manual) |
| `REDIS_PORT` | `6379` | Redis port |

### MQTT

| Variable | Default | Description |
|----------|---------|-------------|
| `MQTT_BROKER` | `tcp://broker.hivemq.com:1883` | MQTT broker URL. Use `ssl://` for TLS |
| `MQTT_CLIENT_ID` | `atlas-mqtt-consumer` | Unique client identifier |
| `MQTT_TOPIC` | `thw/telemetry/#` | Topic subscription pattern. `#` is a wildcard |
| `MQTT_QOS` | `1` | MQTT Quality of Service (0=at most once, 1=at least once, 2=exactly once) |

### Alerting Engine

| Variable | Default | Description |
|----------|---------|-------------|
| `ALERT_SCHEDULER_CRON` | `0 */1 * * * *` | Spring cron for alert evaluation (every 1 minute) |
| `ALERT_TIME_WINDOW_MINS` | `10` | How far back to look for sensor readings (minutes) |
| `ALERT_RETENTION_DAYS` | `1` | How long to keep resolved alerts before deletion (days) |

### Admin Account

| Variable | Default | Description |
|----------|---------|-------------|
| `ADMIN_USERNAME` | `admin` | Seeded admin username |
| `ADMIN_PASSWORD` | `admin123` | Seeded admin password — **change this!** |

### Service Ports

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT_FRONTEND` | `8090` | Host port for the React dashboard |
| `PORT_MQTT_SERVICE` | `8091` | Host port for MQTT ingestion service |
| `PORT_METADATA_SERVICE` | `8092` | Host port for metadata service |
| `PORT_ALERTING_SERVICE` | `8093` | Host port for alerting service |
| `PORT_REPORT_SERVICE` | `8094` | Host port for report service |
| `PORT_USER_SERVICE` | `8096` | Host port for user/auth service |
| `PORT_GIS_SERVICE` | `8097` | Host port for GIS service |
| `PORT_POSTGRES` | `5432` | Host port for TimescaleDB |
| `PORT_REDIS` | `6379` | Host port for Redis |

---

## Service-Specific Configuration

Each service has an `application.yml` (or `application.yaml`) in its `src/main/resources/` directory.

### MQTT Ingestion Service
`mqtt-data-ingestion-service/mqttSubscriber/src/main/resources/application.yml`

```yaml
server:
  port: 8091

mqtt:
  broker: tcp://broker.hivemq.com:1883  # Change to your broker
  client-id: spring-mqtt-consumer
  topic: thw/telemetry/#                 # Change to your topic pattern
  qos: 1

spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/kernelx
    username: kernelx
    password: kernelx
  jpa:
    hibernate:
      ddl-auto: update   # Change to 'validate' in production
```

**Changing the topic pattern:**  
The `#` at the end is an MQTT wildcard meaning "any sub-topic". For example:
- `thw/telemetry/#` matches `thw/telemetry/sensor1`, `thw/telemetry/site-a/sensor-1`, etc.
- `sensors/+/data` matches `sensors/sensor1/data` but not `sensors/site/sensor1/data`

---

### Alerting Service
`disaster-management-alerting-service/src/main/resources/application.yaml`

```yaml
server:
  port: 8093

alert:
  scheduler-cron: "0 */1 * * * *"   # Spring cron: every 1 minute
  time-window-in-mins: 10            # Evaluate readings from last N minutes
  retention-in-days: 1               # Delete resolved alerts older than N days
```

**Cron expression format:**
```
 ┌─── second (0-59)
 │ ┌─── minute (0-59)
 │ │ ┌─── hour (0-23)
 │ │ │ ┌─── day of month (1-31)
 │ │ │ │ ┌─── month (1-12)
 │ │ │ │ │ ┌─── day of week (0-7, 0 and 7 = Sunday)
 │ │ │ │ │ │
 0 */1 * * * *   ← Every minute, on the 0-second mark
 0 */5 * * * *   ← Every 5 minutes
 0 0 * * * *     ← Every hour
```

---

### User/Auth Service
`disaster-management-user-service/src/main/resources/application.yaml`

```yaml
server:
  port: 8096

jwt:
  secret: your-256-bit-hex-secret   # Generate: openssl rand -hex 32
  expiration: 900000                  # Access token: 15 minutes
  refresh-expiration: 86400000        # Refresh token: 1 day

spring:
  data:
    redis:
      host: localhost
      port: 6379
```

**Sharing JWT secret with other services:**  
The Metadata Service and GIS Service validate JWTs using the **same secret** as the User Service. When you change the `JWT_SECRET`, update it everywhere.

---

### Metadata Handling Service
`metadata-handling-service/src/main/resources/application.yml`

```yaml
server:
  port: 8092

spring:
  data:
    redis:
      host: localhost
      port: 6379

springdoc:
  swagger-ui:
    path: /swagger-ui.html   # Swagger UI available at this path
```

---

### GIS Monitoring Service
`gis-monitoring-service/src/main/resources/application.yaml`

```yaml
server:
  port: 8097

spring:
  datasource:
    url: ${SPRING_DATASOURCE_URL:jdbc:postgresql://localhost:5432/kernelx}
    # Supports Docker environment variables with fallback to localhost
```

---

## Sensor Threshold Configuration

Thresholds are stored **per sensor** in the database and are configured via the Metadata API (or Swagger UI). They define when the alert engine creates, escalates, or resolves alerts.

### Threshold hierarchy

```
threshold_high_critical  ← Measurement ABOVE this = HIGH_CRITICAL alert
threshold_high_warning   ← Measurement ABOVE this = HIGH_WARNING alert
        [NORMAL RANGE]
threshold_low_warning    ← Measurement BELOW this = LOW_WARNING alert
threshold_low_critical   ← Measurement BELOW this = LOW_CRITICAL alert
```

### Example threshold values by sensor type

| Sensor Type | Unit | High Critical | High Warning | Low Warning | Low Critical |
|-------------|------|--------------|-------------|------------|--------------|
| Water Level Sensor | m | 8.0 | 6.0 | 2.0 | 1.0 |
| Temperature Sensor | °C | 38.0 | 34.0 | 18.0 | 14.0 |
| Wind Speed Sensor | km/h | 60.0 | 45.0 | 5.0 | 2.0 |
| Rainfall Sensor | mm | 250.0 | 180.0 | 10.0 | 0.0 |
| Air Quality Sensor | µg/m³ | 150.0 | 100.0 | 10.0 | 0.0 |

---

## Frontend Configuration

The frontend uses **Nginx** as a reverse proxy in Docker. The Nginx config lives at:  
`disaster-management-frontend/nginx.conf`

This file handles:
- Serving the React SPA on port 80
- Proxying API requests to backend services
- CORS headers

**Update proxy targets** in `nginx.conf` if your service ports change:
```nginx
location /disaster-management/ {
    proxy_pass http://gis-monitoring-service:8097;
}
location /api/ {
    proxy_pass http://user-service:8096;
}
```

---

## TimescaleDB Data Retention

For long-running deployments, configure TimescaleDB retention policies to prevent unbounded data growth:

```sql
-- Connect to the database
docker exec -it master_timescaledb psql -U kernelx -d kernelx

-- Create a retention policy: delete sensor_readings older than 1 year
SELECT add_retention_policy('sensor_readings', INTERVAL '1 year');

-- Check existing policies
SELECT * FROM timescaledb_information.jobs;
```

> Adjust retention based on your storage capacity and regulatory requirements.
