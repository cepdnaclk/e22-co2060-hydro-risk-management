<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f4c75,50:1b6ca8,100:0f4c75&height=220&section=header&text=ATLAS&fontSize=80&fontColor=ffffff&fontAlignY=38&desc=Adaptive%20Time-Series%20Analytics%20and%20Logging%20System&descAlignY=62&descSize=20&animation=fadeIn" width="100%" alt="ATLAS — Adaptive Time-Series Analytics and Logging System" />
</div>



# 🌍 ATLAS – Adaptive Time-Series Analytics and Logging System
### Domain‑Agnostic Government Monitoring Platform
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-3C52F0?style=for-the-badge&logo=mqtt&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

<p align="center">
  <img width="800" height="500" alt="readme image" src="https://github.com/user-attachments/assets/e8e19beb-3360-48b2-b968-06bea651055e" />
</p>

**ATLAS** is a domain‑agnostic monitoring and management platform designed to be adapted by multiple government organizations. While the primary use case is **Integrated Hydro Risk Management**, the system is architected to support any domain requiring real-time measurements, historical analytics, and asset management.

## ✨ Core Features

<div align="center">

| | | |
|:---:|:---:|:---:|
|  🚨<br/>**Real-time Alerts**<br/><sub>Responsive interface for visualizing risk alerts and monitoring trends</sub> |  📡<br/>**Automated Data Ingestion**<br/><sub>Seamless MQTT-based processing of field sensor data</sub> |  🗂️<br/>**Metadata Management**<br/><sub>Full CRUD interfaces for disaster-related entities and configurations</sub> |
|  🧩<br/>**Microservices Architecture**<br/><sub>Decoupled backend services built for modularity and scalability</sub> |  🗺️<br/>**GIS-Based Dashboard**<br/><sub>Integrated mapping for spatial awareness of distributed field assets</sub> |  🔐<br/>**Role-Based Access & Secure Login**<br/><sub>Robust authentication and authorization across administrative levels</sub> |
|  📄<br/>**Reporting Service**<br/><sub>Automated periodic reports and data summaries for decision-makers</sub> |  📊<br/>**Analytics Dashboard**<br/><sub>Telemetry charts, battery status, and health scores at a glance</sub> |  ⚡<br/>**Domain-Agnostic by Design**<br/><sub>Adapt to any monitoring domain without re-architecting</sub> |

<br>

![Project Gallery Showcase](docs/images/ATLAS_Dashboard.gif)


</div>

  * **Real-time Alerts**: A modern, responsive interface for visualizing risk alerts and   monitoring trends.<br>

  * **Automated Data Ingestion**: Seamless MQTT-based processing of field sensor data.<br>

  * **Metadata Management**: Full CRUD interfaces to manage disaster-related entities and configurations.<br>

  * **Microservices Architecture**: Decoupled backend services designed for modularity and scalability.<br>

  * **GIS‑Based Dashboard**: Integrated mapping for spatial awareness and real-time visualization of distributed field assets.<br>

  * **Role-Based Access & Secure Login**: Robust authentication and authorization to ensure data security across different administrative levels.<br>

  * **Reporting Service**: Automated generation of periodic reports and data summaries for decision-makers.<br>
  
  * **Analytics dashboard**: System status monitoring interactive dashboard with telemetry charts, battery status, and health scores<br>



---

## Data Flow within Application

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Segoe UI, sans-serif','actorBkg':'#dbeafe','actorBorder':'#2563eb','actorTextColor':'#1e3a8a','noteBkgColor':'#fef3c7','noteBorderColor':'#d97706','signalColor':'#475569'}}}%%
sequenceDiagram
    autonumber
    participant Sensor as Field Sensor
    participant MQTT as MQTT Broker
    participant Ingest as Ingestion Service
    participant DB as TimescaleDB
    participant Alert as Alert Engine
    participant FE as Dashboard

    rect rgb(240, 253, 244)
    Note over Sensor,DB: INGESTION PIPELINE
    Sensor->>MQTT: Publish {deviceId, value, timestamp, battery}
    MQTT->>Ingest: Subscribe callback (QoS 1)
    Ingest->>Ingest: Validate + buffer in ConcurrentQueue
    Note over Ingest:  Batch flush every predetermined seconds
    Ingest->>DB: saveAll(batch)
    end

    rect rgb(254, 242, 242)
    Note over Alert,DB: ALERT EVALUATION
    loop Every cron cycle
        Alert->>DB: Query readings in last 10-min window
        Alert->>Alert: Compare vs sensor thresholds
        Alert->>DB: Create / Escalate / Resolve alerts
    end
    end

    rect rgb(253, 242, 248)
    Note over FE,DB: LIVE DASHBOARD
    FE->>DB: GET /sensors, /latest-all, /alerts/active
    DB-->>FE: Return live data
    FE->>FE: Render dashboard, GIS map, charts
    end
```

---

## 📁 Repository Structure

```
e22-co2060-hydro-risk-management/          ← Main orchestration repo
│
├──  README.md                           ← You are here
├──  docker-compose.yml                  ← One-command full-stack launch
├──  .env.example                        ← Environment variable template
├──  LICENSE                             ← MIT License
├──  CONTRIBUTING.md                     ← Contribution guide
├──  SECURITY.md                         ← Security policy
├──  CHANGELOG.md                        ← Version history
│
├──  .github/
│   ├──  ISSUE_TEMPLATE/                 ← Bug report & feature request forms
│   ├──  PULL_REQUEST_TEMPLATE.md        ← PR checklist
│   └──  workflows/ci.yml               ← GitHub Actions CI pipeline
│
├──  docs/
│   ├──  ARCHITECTURE.md                 ← Deep-dive system design & diagrams
│   ├──  DEPLOYMENT.md                   ← Docker, manual & cloud deployment
│   ├──  CONFIGURATION.md                ← All environment & config options
│   ├──  API_REFERENCE.md               ← REST API documentation
│   └──  PROJECT_GUIDE.md               ← Quick start & feature guide
│
├──  additional-files/
│   └──  SensorEmulator_*.zip            ← Windows MQTT test publisher
│
│   ── Git Submodules (each an independent repo) ──────────────────
│
├──  mqtt-data-ingestion-service/        ← MQTT subscriber + TimescaleDB writer
├──  metadata-handling-service/          ← Sites, Sensors, SensorTypes CRUD
├──  disaster-management-alerting-service/ ← Threshold alert engine
├──  report-generating-service/          ← PDF report generation
├──  disaster-management-user-service/   ← Auth, JWT, RBAC
├──  gis-monitoring-service/             ← GIS & telemetry read API
└──  disaster-management-frontend/       ← React 19 dashboard (Vite + Nginx)
```
---




## 🏗️ System Architecture

```mermaid

%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter, Segoe UI, sans-serif','primaryColor':'#e0f2fe','primaryBorderColor':'#0284c7','lineColor':'#64748b','fontSize':'14px'}}}%%
graph TB
    subgraph SRC["📡 DATA SOURCES"]
        direction LR
        S1[" Temperature<br/>Sensor"]
        S2[" Water Level<br/>Sensor"]
        S3[" Rainfall<br/>Sensor"]
        S4[" Wind Speed<br/>Sensor"]
        EMU[" Sensor Emulator<br/>Windows / Python"]
    end

    subgraph BRK["☁️ MESSAGE BROKER"]
        MQTT[" MQTT Broker<br/>broker.hivemq.com"]
    end

    subgraph SVC["⚙️ BACKEND MICROSERVICES"]
        direction LR
        MS1[" MQTT Ingestion<br/><b>:8091</b><br/>Paho · Batch Write"]
        MS2[" Metadata<br/><b>:8092</b><br/>Sites · Sensors · Types"]
        MS3[" Alerting<br/><b>:8093</b><br/>Threshold Engine · Cron"]
        MS4[" Report<br/><b>:8094</b><br/>PDF · iText"]
        MS5[" User Auth<br/><b>:8096</b><br/>JWT · RBAC"]
        MS6[" GIS<br/><b>:8097</b><br/>Map Data · Telemetry"]
    end

    subgraph DAT["🗄️ DATA LAYER"]
        direction LR
        DB[(" TimescaleDB<br/>PostgreSQL :5432<br/>kernelx database")]
        REDIS[(" Redis Cache<br/>:6379<br/>Token Blacklist")]
    end

    subgraph FRT[" FRONTEND"]
        FE["⚛️ React 19 Dashboard<br/><b>:8090</b><br/>Ant Design · Leaflet · Recharts"]
    end

    S1 & S2 & S3 & S4 & EMU -->|" Publish"| MQTT
    MQTT -->|" Subscribe"| MS1
    MS1 & MS2 & MS3 & MS4 & MS5 & MS6 <-->|"JPA / SQL"| DB
    MS5 & MS2 <-->|"Token Blacklist"| REDIS
    FE -->|"REST API"| MS2 & MS3 & MS4 & MS5 & MS6

    classDef sensor fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    classDef broker fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f
    classDef service fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a
    classDef alert fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d
    classDef data fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#4c1d95
    classDef front fill:#fce7f3,stroke:#db2777,stroke-width:2px,color:#831843

    class S1,S2,S3,S4,EMU sensor
    class MQTT broker
    class MS1,MS2,MS4,MS5,MS6 service
    class MS3 alert
    class DB,REDIS data
    class FE front

    style SRC fill:#f0fdf4,stroke:#16a34a,stroke-dasharray: 5 5
    style BRK fill:#fffbeb,stroke:#d97706,stroke-dasharray: 5 5
    style SVC fill:#eff6ff,stroke:#2563eb,stroke-dasharray: 5 5
    style DAT fill:#f5f3ff,stroke:#7c3aed,stroke-dasharray: 5 5
    style FRT fill:#fdf2f8,stroke:#db2777,stroke-dasharray: 5 5
  
```


### Service Reference

| Service | Port | Tech Stack | Description |
|---------|------|-----------|-------------|
| [MQTT Ingestion](mqtt-data-ingestion-service/) | 8091 | Spring Boot 4, Eclipse Paho, TimescaleDB | Subscribes to MQTT topic, validates, buffers and batch-writes sensor telemetry |
| [Metadata Service](metadata-handling-service/) | 8092 | Spring Boot 4, PostgreSQL, Redis, Swagger | Full CRUD API for Sites, Sensors, and SensorTypes with JWT protection |
| [Alerting Service](disaster-management-alerting-service/) | 8093 | Spring Boot 4, PostgreSQL, Spring Scheduler | Cron-based engine that creates, escalates, and resolves threshold alerts |
| [Report Service](report-generating-service/) | 8094 | Spring Boot 4, iText, Thymeleaf, PostgreSQL | Generates downloadable PDF reports from historical telemetry and alert data |
| [User/Auth Service](disaster-management-user-service/) | 8096 | Spring Boot 4, JWT, Spring Security, Redis | Authentication, JWT token management, and role-based access control |
| [GIS Service](gis-monitoring-service/) | 8097 | Spring Boot 4, PostgreSQL | Read-only API serving sensor positions and telemetry for the map dashboard |
| [Frontend](disaster-management-frontend/) | 8090 | React 19, Vite, Ant Design 5, Leaflet, Recharts | Interactive monitoring dashboard with GIS map and analytics |

<br>

### Tech Stack

<div>

<table>
<thead>
<tr>
<th colspan="2" align="center">Frontend</th>
<th colspan="2" align="center">Backend</th>
<th colspan="2" align="center">Infrastructure</th>
</tr>
<tr>
<th align="left">Component</th>
<th align="left" width="230">Technology</th>
<th align="left">Component</th>
<th align="left" width="230">Technology</th>
<th align="left">Component</th>
<th align="left" width="230">Technology</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>Framework</b></td>
<td align="left"><img src="https://img.shields.io/badge/React_19-20232A?style=flat-square&logo=react&logoColor=61DAFB" alt="React 19"/> <img src="https://img.shields.io/badge/Vite_7-646CFF?style=flat-square&logo=vite&logoColor=white" alt="Vite 7"/></td>
<td><b>Framework</b></td>
<td align="left"><img src="https://img.shields.io/badge/Spring_Boot_4.0-6DB33F?style=flat-square&logo=springboot&logoColor=white" alt="Spring Boot 4.0"/></td>
<td><b>Containerization</b></td>
<td align="left"><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker"/> <img src="https://img.shields.io/badge/Docker_Compose-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker Compose"/></td>
</tr>
<tr>
<td><b>Language</b></td>
<td align="left"><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript"/><br/><img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/></td>
<td><b>Language</b></td>
<td align="left"><img src="https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white" alt="Java 21"/></td>
<td><b>Web Server</b></td>
<td align="left"><img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white" alt="Nginx"/><br/><sub><i>Frontend</i></sub></td>
</tr>
<tr>
<td><b>UI Library</b></td>
<td align="left"><img src="https://img.shields.io/badge/Ant_Design_5-0170FE?style=flat-square&logo=antdesign&logoColor=white" alt="Ant Design 5"/></td>
<td><b>Database</b></td>
<td align="left"><img src="https://img.shields.io/badge/PostgreSQL_14-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL 14"/><br/><img src="https://img.shields.io/badge/TimescaleDB-FDB515?style=flat-square&logo=timescale&logoColor=black" alt="TimescaleDB"/></td>
<td><b>Time-series DB</b></td>
<td align="left"><img src="https://img.shields.io/badge/TimescaleDB-FDB515?style=flat-square&logo=timescale&logoColor=black" alt="TimescaleDB"/><br/><sub><i>PostgreSQL extension</i></sub></td>
</tr>
<tr>
<td><b>Maps</b></td>
<td align="left"><img src="https://img.shields.io/badge/React_Leaflet-199900?style=flat-square&logo=leaflet&logoColor=white" alt="React Leaflet"/></td>
<td><b>Cache</b></td>
<td align="left"><img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis"/></td>
<td><b>Message Broker</b></td>
<td align="left"><img src="https://img.shields.io/badge/HiveMQ_(public)-FFC000?style=flat-square&logo=hivemq&logoColor=black" alt="HiveMQ (public)"/><br/>or any MQTT broker</td>
</tr>
<tr>
<td><b>Charts</b></td>
<td align="left"><img src="https://img.shields.io/badge/Recharts-22B5BF?style=flat-square&logo=react&logoColor=white" alt="Recharts"/></td>
<td><b>Security</b></td>
<td align="left"><img src="https://img.shields.io/badge/Spring_Security-6DB33F?style=flat-square&logo=springsecurity&logoColor=white" alt="Spring Security"/><br/><img src="https://img.shields.io/badge/JJWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JJWT"/></td>
<td></td><td></td>
</tr>
<tr>
<td><b>HTTP Client</b></td>
<td align="left"><img src="https://img.shields.io/badge/Axios-5A29E4?style=flat-square&logo=axios&logoColor=white" alt="Axios"/></td>
<td><b>MQTT Client</b></td>
<td align="left"><img src="https://img.shields.io/badge/Eclipse_Paho-660066?style=flat-square&logo=mqtt&logoColor=white" alt="Eclipse Paho"/></td>
<td></td><td></td>
</tr>
<tr>
<td><b>Routing</b></td>
<td align="left"><img src="https://img.shields.io/badge/React_Router_7-CA4245?style=flat-square&logo=reactrouter&logoColor=white" alt="React Router 7"/></td>
<td><b>PDF Generation</b></td>
<td align="left"><img src="https://img.shields.io/badge/iText-E34F26?style=flat-square&logo=adobeacrobatreader&logoColor=white" alt="iText"/><br/><img src="https://img.shields.io/badge/Thymeleaf-005F0F?style=flat-square&logo=thymeleaf&logoColor=white" alt="Thymeleaf"/></td>
<td></td><td></td>
</tr>
<tr>
<td></td><td></td>
<td><b>API Docs</b></td>
<td align="left"><img src="https://img.shields.io/badge/SpringDoc_OpenAPI-85EA2D?style=flat-square&logo=swagger&logoColor=black" alt="SpringDoc OpenAPI"/></td>
<td></td><td></td>
</tr>
<tr>
<td></td><td></td>
<td><b>Build</b></td>
<td align="left"><img src="https://img.shields.io/badge/Maven-C71A36?style=flat-square&logo=apachemaven&logoColor=white" alt="Maven"/></td>
<td></td><td></td>
</tr>
</tbody>
</table>

</div>

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 📊 Analytics Dashboard
- System health score gauge
- Battery level distribution chart
- Reading occurrence timeline
- Threshold status breakdown
- Sensor table with search, filter, and sort
- Per-sensor historical trend drawer
- Auto-refresh every 30 seconds

</td>
<td width="50%">

### 🗺️ GIS Map Dashboard
- Interactive Leaflet map (OpenStreetMap)
- Color-coded sensor markers by alert severity
- Animated pulse effect on active alerts
- Sensor search autocomplete
- Fly-to animation on sensor selection
- Detail drawer with telemetry chart

</td>
</tr>
<tr>
<td>

### 🚨 Alerting Engine
- Cron-based updates cycle
- 4-level severity hierarchy
- Escalation and de-escalation
- Auto-resolution when normal
- Configurable alert retention
- Sliding time-window evaluation

</td>
<td>

### 🔐 Security
- JWT access tokens (15 min)
- Refresh tokens (1 day, HttpOnly cookie)
- Redis-backed token blacklisting
- Role-based access (ADMIN / USER)
- Auto token refresh on 401
- Seeded admin account on first boot

</td>
</tr>
</table>

---

## ⚡ Quick Start

Get the full platform running locally in under 5 minutes:

```bash
# 1. Clone with all submodules
git clone --recurse-submodules https://github.com/cepdnaclk/e22-co2060-hydro-risk-management.git
cd e22-co2060-hydro-risk-management

# 2. Configure your environment
cp .env.example .env
# Edit .env: set POSTGRES_PASSWORD, JWT_SECRET, ADMIN_PASSWORD

# 3. Launch the entire 9-container stack
docker compose up --build -d

# 4. Open the dashboard
# http://localhost:8090  →  Login: admin / admin123
```

> **First boot:** Takes ~3–5 minutes while TimescaleDB initializes and Spring Boot services start. Services auto-retry connections.

### Access Points

| Service | URL | Notes |
|---------|-----|-------|
| 🌐 **Dashboard** | http://localhost:8090 | `admin` / `admin123` |
| 📋 **Metadata API Swagger** | http://localhost:8092/swagger-ui.html | Interactive API docs |
| 👤 **Auth API Swagger** | http://localhost:8096/swagger-ui.html | Interactive API docs |


---

## 📖 Documentation Index

| Document | Description |
|----------|-------------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | Deep-dive system design — service internals, DB schema, security flows, design decisions |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Docker Compose, manual, cloud (AWS, GKE, Swarm), production checklist |
| [API_REFERENCE.md](API_REFERENCE.md) | Complete REST API docs for all 6 backend services with request/response examples |
| [CONFIGURATION.md](CONFIGURATION.md) | All environment variables, application.yml options, and config reference |
| [PROJECT_GUIDE.md](PROJECT_GUIDE.md) | Quick-start guide, alert system explained, domain adaptation steps |
| [SECURITY.md](SECURITY.md) | Security policy, production hardening checklist, responsible disclosure |

---



## 👥 Team - KernelX

| Member | ID | Contact |
|--------|----|---------|
| Dinith Kariyawasam | E/22/182 | e22182@eng.pdn.ac.lk |
| Rameesha Prathapasinghe | E/22/291 | e22291@eng.pdn.ac.lk |
| Tharindu Weerasinghe | E/22/421 | e22421@eng.pdn.ac.lk |
| Gayumi Wimalaweera | E/22/449 | e22449@eng.pdn.ac.lk |

**Supervised by:** Prof. Kamalanath Samarakoon  
**Module:** CO2060 Software Systems Design  
**Department of Computer Engineering, University of Peradeniya**


---

