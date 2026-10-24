# Changelog

---

## [Unreleased]

### Planned
- WebSocket-based real-time alert push notifications
- API Gateway (Nginx / Spring Cloud Gateway) for centralized routing
- Kubernetes deployment manifests
- TimescaleDB continuous aggregates for long-term analytics
- Email/SMS alert notification integrations
- Multi-language (i18n) support for the dashboard

---

## [1.0.0] — 2025-10-24

### 🎉 Initial Release

#### Added

**Core Infrastructure**
- Docker Compose orchestration for all 9 services (db, redis, 6 backend services, frontend)
- Environment variable configuration via `.env` file
- Health checks on all critical services (`db`, `redis`)
- Auto-restart policies (`restart: unless-stopped`) on all services

**MQTT Data Ingestion Service** (Port 8091)
- Eclipse Paho MQTT client connecting to configurable broker
- Thread-safe in-memory buffer (`ConcurrentLinkedQueue`) for received messages
- Batch write to TimescaleDB every 8 seconds via `@Scheduled`
- Bean Validation on incoming telemetry payloads
- Graceful shutdown flush (`@PreDestroy`)
- Persistent MQTT session with auto-reconnect

**Metadata Handling Service** (Port 8092)
- Full CRUD REST API for Sites, Sensors, and SensorTypes
- Per-sensor threshold configuration (High Critical, High Warning, Low Warning, Low Critical)
- JWT authentication on write endpoints
- Redis-backed token blacklist validation
- OpenAPI (Swagger) documentation

**Alerting Service** (Port 8093)
- Scheduled alert evaluation engine (every 1 minute, configurable cron)
- Sliding 10-minute evaluation window
- 4-level severity: `HIGH_CRITICAL`, `HIGH_WARNING`, `LOW_WARNING`, `LOW_CRITICAL`
- Alert escalation and de-escalation on severity change
- Auto-resolution when sensor returns to normal range
- Configurable alert retention period
- DDD (Domain-Driven Design) layered architecture
- Integration and unit test suite with Testcontainers

**Report Generating Service** (Port 8094)
- PDF report generation for telemetry data and alert history
- Thymeleaf HTML templates rendered to PDF via iText
- Date-range filtered reports
- Support for: Telemetry Report, Alert Report

**User / Auth Service** (Port 8096)
- JWT authentication (15-minute access token, 1-day refresh token)
- Role-Based Access Control (RBAC): `ADMIN` and `USER` roles
- Redis-backed token blacklisting for logout and refresh invalidation
- Full user CRUD for admins
- Password change functionality
- DataSeeder for initial admin account
- OpenAPI (Swagger) documentation

**GIS Monitoring Service** (Port 8097)
- Read-only aggregation API for GIS map rendering
- Sensor list with coordinates endpoint
- Latest telemetry per sensor (batch and individual)
- Historical telemetry with configurable time ranges (1h, 24h, 7d, 30d)
- Active alerts endpoint

**Frontend** (Port 8090)
- React 19 + Vite SPA served via Nginx
- Dark/Light mode toggle (persisted in localStorage)
- JWT auto-refresh interceptor on all API calls
- `ProtectedRoute` with role-based access guard

- **GIS Dashboard** — Interactive Leaflet map with OpenStreetMap tiles, pulsing severity-coded sensor markers, sensor search autocomplete, flyTo animations, detail drawer with telemetry chart
- **Analytics Dashboard** — System health gauge, battery distribution chart, reading occurrence timeline scatter chart, threshold breakdown donut chart, searchable/filterable sensor table, per-sensor trend drawer with time range selector, auto-refresh every 30 seconds
- **Alerts Page** — Active alert list with severity indicators
- **Telemetry Data Page** — Raw sensor reading browser
- **Reports Page** — PDF report generation UI
- **Metadata Pages** — CRUD interfaces for Sites, Sensor Types, and Sensors
- **User Management** — Admin-only user CRUD page
- **Profile Page** — User profile and password change
- Mock data fallback for all API services (demo without backend)

**Documentation**
- Comprehensive `README.md` with architecture diagrams, quick start, and feature overview
- `docs/ARCHITECTURE.md` — Deep-dive system design guide with Mermaid diagrams
- `docs/DEPLOYMENT.md` — Docker, manual, and cloud deployment guides
- `docs/CONFIGURATION.md` — Complete configuration reference
- `docs/API_REFERENCE.md` — REST API documentation with request/response examples
- `SECURITY.md` — Security policy and production hardening checklist
- `.env.example` — Annotated environment variable template



---


