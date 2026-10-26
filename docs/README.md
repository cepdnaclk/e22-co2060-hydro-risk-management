---
layout: home
permalink: index.html
repository-name: e22-co2060-hydro-risk-management
title: ATLAS – Adaptive Time-Series Analytics and Logging System
---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f4c75,50:1b6ca8,100:0f4c75&height=220&section=header&text=ATLAS&fontSize=80&fontColor=ffffff&fontAlignY=38&desc=Adaptive%20Time-Series%20Analytics%20and%20Logging%20System&descAlignY=62&descSize=20&animation=fadeIn" width="100%" alt="ATLAS — Adaptive Time-Series Analytics and Logging System" />

<img width="900" height="531" alt="Image" src="https://github.com/user-attachments/assets/f277d23a-83e9-402c-bb13-f0f0df324c28" />

<br>


<p>
  <img src="https://img.shields.io/badge/React_19-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React 19"/>
  <img src="https://img.shields.io/badge/Spring_Boot_4-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white" alt="Spring Boot"/>
  <img src="https://img.shields.io/badge/TimescaleDB-FDB515?style=for-the-badge&logo=timescale&logoColor=black" alt="TimescaleDB"/>
  <img src="https://img.shields.io/badge/MQTT-3C52F0?style=for-the-badge&logo=mqtt&logoColor=white" alt="MQTT"/>
  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Java_21-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white" alt="Java 21"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Status-Production_Ready-brightgreen?style=flat-square" alt="Status"/>
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square" alt="Version"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License"/>
  <img src="https://img.shields.io/badge/Services-7_Microservices-purple?style=flat-square" alt="Services"/>
  <img src="https://img.shields.io/badge/University_of_Peradeniya-CO2060-red?style=flat-square" alt="University"/>
</p>

<br/>

**A production-grade, domain-agnostic IoT monitoring and risk management platform**<br/>
*built for government and critical infrastructure — from rivers to smart cities.*

<br/>

</div>




# ATLAS – Adaptive Time-Series Analytics and Logging System  
### Domain-Agnostic Government Monitoring Platform


## Team

-  E/22/182, Dinith Kariyawasam, [e22182@eng.pdn.ac.lk](mailto:e22182@eng.pdn.ac.lk)
-  E/22/291, Rameesha Prathapasinghe, [e22291@eng.pdn.ac.lk](mailto:e22182@eng.pdn.ac.lk)
-  E/22/421, Tharindu Weerasinghe, [e22421@eng.pdn.ac.lk](mailto:e22182@eng.pdn.ac.lk)
-  E/22/449, Gayumi Wimalaweera, [e22449@eng.pdn.ac.lk](mailto:e22182@eng.pdn.ac.lk)


**Supervised by:** Prof. Kamalanath Samarakoon  
**Module:** CO2060 – Software Systems Design  
**Department of Computer Engineering, University of Peradeniya, Sri Lanka**


#### Table of Contents
1. [Introduction](#introduction)
2. [Live Dashboard Preview](#live-dashboard-preview)
3. [System Design](#system-design)
4. [System Architecture](#system-architecture)
5. [Feature Deep Dive](#feature-deep-dive)
6. [End Product](#end-product)
7. [Conclusion](#conclusion)

<br>

---

## Introduction

**ATLAS (Adaptive Time-Series Analytics and Logging System)** is a **domain-agnostic monitoring and management platform** designed to be adapted by multiple government organizations.

While the primary use case is **Integrated Hydro Risk Management**, the system is architected to support any domain requiring:

- Real-time measurements from field assets  
- Historical data analytics  
- Asset and infrastructure management  
- Scalable monitoring and reporting systems  

The platform connects **IoT field sensors → MQTT message broker → intelligent backend services → interactive GIS dashboard**, delivering a complete real-time situational awareness system for decision-makers and field operators.

ATLAS enables:

- Real-time and periodic data collection  
- Centralized logging and storage of time-series data  
- Efficient asset and metadata management  
- Scalable and modular system expansion  

The **ATLAS (Adaptive Time-Series Analytics and Logging System)** is a full-stack, microservices-based monitoring platform engineered for **Integrated Hydro Risk Management**: with the architectural flexibility to serve **any domain** involving field sensors, real-time data, and risk alerting platform.

*Domains ATLAS can serve out-of-the-box:*

| Domain | Sensor Types | Alert Meaning |
|--------|-------------|---------------|
| 🌊 Hydro Risk | Water level, Rainfall, Flow rate | Flood / drought alerts |
| 💧 Irrigation | Soil moisture, Tank level, Flow | Water stress / overflow |
| 🌿 Environment | Air quality, CO2, PM2.5, Temperature | Pollution thresholds |
| ⚡ Power Grid | Voltage, Current, Load | Outage / overload risk |
| 🏙️ Smart City | Traffic density, Noise, Humidity | Congestion / comfort |
| 🏭 Industrial | Pressure, Vibration, Temperature | Equipment fault detection |


> Originally developed as the primary use case for **flood and hydrological risk monitoring** across Sri Lankan river systems, ATLAS is built to scale seamlessly into irrigation networks, power distribution, environmental monitoring, and smart city infrastructure.



---


## Live Dashboard Preview

<div align="center">

![ATLAS Dashboard in Action](images/ATLAS_Dashboard.gif)

*Real-time GIS mapping, telemetry analytics, and intelligent alert management - all in one platform*

</div>



<div align="center">

| | | |
|:---:|:---:|:---:|
| **GIS Live Map**<br/><sub>Interactive Leaflet map with animated, severity-coded sensor markers and fly-to animations</sub> | **MQTT Data Ingestion**<br/><sub>Persistent, auto-reconnecting subscriber with batch writes to TimescaleDB every 8 seconds</sub> | **4-Level Alert Engine**<br/><sub>Cron-based sliding-window evaluation with escalation, de-escalation, and auto-resolution</sub> |
| **Analytics Dashboard**<br/><sub>Health score gauges, battery charts, occurrence timelines, threshold donut charts — auto-refreshed</sub> | **JWT + RBAC Security**<br/><sub>15-min access tokens, HttpOnly refresh cookies, Redis blacklisting, and role-gated routes</sub> | **PDF Report Generation**<br/><sub>Download telemetry and alert history reports for any date range via iText + Thymeleaf</sub> |
| **Microservices Architecture**<br/><sub>7 independently deployable services, each owning its domain — orchestrated by Docker Compose</sub> | **Domain-Agnostic**<br/><sub>Adapt to any sensor domain without touching core code — just register types, sites, and thresholds</sub> | **One-Command Deployment**<br/><sub>`docker compose up --build -d` launches the entire 9-container stack in under 5 minutes</sub> |

</div>


<br>

---

## System Design

### Real-Time Data Flow

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
    Note over Ingest: Batch flush every 8 seconds
    Ingest->>DB: saveAll(batch) → TimescaleDB hypertable
    end

    rect rgb(254, 242, 242)
    Note over Alert,DB: ALERT EVALUATION
    loop Every 1 minute (cron)
        Alert->>DB: Query sensor_readings in last 10-min window
        Alert->>Alert: Compare latest reading vs sensor thresholds
        Alert->>DB: Create / Escalate / Resolve alerts
    end
    end

    rect rgb(253, 242, 248)
    Note over FE,DB: LIVE DASHBOARD (auto-refresh 30s)
    FE->>DB: GET /sensors, /telemetry/latest-all, /alerts/active
    DB-->>FE: Return live sensor + alert data
    FE->>FE: Render GIS map, charts, KPI cards
    end
```

<br>

### Technology Stack

<div>

<table>
<thead>
<tr>
<th colspan="2" align="center">Frontend</th>
<th colspan="2" align="center">Backend</th>
<th colspan="2" align="center">Infrastructure</th>
</tr>
</thead>
<tbody>
<tr>
<td>Framework</td>
<td><img src="https://img.shields.io/badge/React_19-20232A?style=flat-square&logo=react&logoColor=61DAFB"/> <img src="https://img.shields.io/badge/Vite_7-646CFF?style=flat-square&logo=vite&logoColor=white"/></td>
<td>Framework</td>
<td><img src="https://img.shields.io/badge/Spring_Boot_4.0-6DB33F?style=flat-square&logo=springboot&logoColor=white"/></td>
<td>Containers</td>
<td><img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/> <img src="https://img.shields.io/badge/Compose-2496ED?style=flat-square&logo=docker&logoColor=white"/></td>
</tr>
<tr>
<td>Language</td>
<td><img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/></td>
<td>Language</td>
<td><img src="https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/></td>
<td>Web Server</td>
<td><img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white"/></td>
</tr>
<tr>
<td>UI Library</td>
<td><img src="https://img.shields.io/badge/Ant_Design_5-0170FE?style=flat-square&logo=antdesign&logoColor=white"/></td>
<td>Database</td>
<td><img src="https://img.shields.io/badge/TimescaleDB-FDB515?style=flat-square&logo=timescale&logoColor=black"/> <img src="https://img.shields.io/badge/PostgreSQL_14-4169E1?style=flat-square&logo=postgresql&logoColor=white"/></td>
<td>Broker</td>
<td><img src="https://img.shields.io/badge/HiveMQ-FFC000?style=flat-square&logo=hivemq&logoColor=black"/></td>
</tr>
<tr>
<td>Maps</td>
<td><img src="https://img.shields.io/badge/React_Leaflet-199900?style=flat-square&logo=leaflet&logoColor=white"/></td>
<td>Cache</td>
<td><img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/></td>
<td>CI/CD</td>
<td><img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white"/></td>
</tr>
<tr>
<td>Charts</td>
<td><img src="https://img.shields.io/badge/Recharts-22B5BF?style=flat-square&logo=react&logoColor=white"/></td>
<td>Security</td>
<td><img src="https://img.shields.io/badge/Spring_Security-6DB33F?style=flat-square&logo=springsecurity&logoColor=white"/> <img src="https://img.shields.io/badge/JJWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white"/></td>
<td></td><td></td>
</tr>
<tr>
<td>HTTP</td>
<td><img src="https://img.shields.io/badge/Axios-5A29E4?style=flat-square&logo=axios&logoColor=white"/></td>
<td>MQTT</td>
<td><img src="https://img.shields.io/badge/Eclipse_Paho-660066?style=flat-square&logo=mqtt&logoColor=white"/></td>
<td></td><td></td>
</tr>
<tr>
<td>Router</td>
<td><img src="https://img.shields.io/badge/React_Router_7-CA4245?style=flat-square&logo=reactrouter&logoColor=white"/></td>
<td>PDF</td>
<td><img src="https://img.shields.io/badge/iText-E34F26?style=flat-square&logo=adobeacrobatreader&logoColor=white"/> <img src="https://img.shields.io/badge/Thymeleaf-005F0F?style=flat-square&logo=thymeleaf&logoColor=white"/></td>
<td></td><td></td>
</tr>
</tbody>
</table>

</div>



---



## System Architecture

The platform follows a clean microservices topology with a shared TimescaleDB at the core, fronted by a React 19 SPA served through Nginx.


| Service | Tech Stack | Responsibility |
|---------|-----------|----------------|
| **MQTT Ingestion** | Spring Boot 4, Eclipse Paho, TimescaleDB | Subscribes to MQTT topic; validates, buffers, and batch-writes sensor telemetry into hypertables |
| **Metadata Service** | Spring Boot 4, PostgreSQL, Redis, Swagger | Full CRUD REST API for Sites, Sensors, and SensorTypes with JWT protection and OpenAPI docs |
| **Alerting Service** | Spring Boot 4, PostgreSQL, Spring Scheduler | Cron-based DDD engine that creates, escalates, and auto-resolves 4-level threshold alerts |
| **Report Service** | Spring Boot 4, iText, Thymeleaf, PostgreSQL | Generates downloadable PDF reports from historical telemetry and alert data |
| **User/Auth Service** | Spring Boot 4, JWT, Spring Security, Redis | Authentication, JWT lifecycle management, Redis-backed blacklisting, and RBAC |
| **GIS Service** | Spring Boot 4, PostgreSQL | Read-optimized aggregation API serving sensor positions, telemetry, and alerts for the map |
| **Frontend** | React 19, Vite 7, Ant Design 5, Leaflet, Recharts | Interactive monitoring SPA with GIS map, analytics charts, and metadata management |


<br>


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

<div align="center">

*ATLAS System Architecture Diagram*
</div>

### Architecture and Design Decisions

1. **Shared TimescaleDB**: A single shared database simplifies the architecture, enables easy joins across services, and centralizes backups.

2. **TimescaleDB Extension**: The TimescaleDB extension provides efficient time-series querying and automatic time-based data partitioning.

3. **Public MQTT Broker**: A public MQTT broker eliminates the need to manage broker infrastructure during development and demonstrations.

4. **Cron-Based Alerting (Pull)**: Periodic cron-based evaluation keeps alerting simple, stateless, and easy to restart.

5. **Buffer and Batch Write**: Buffering incoming MQTT messages and writing them in batches protects the database from high-frequency data bursts.

6. **Domain-Driven Design (DDD) in the Alerting Service**: Separating domain, application, and infrastructure layers improves modularity, maintainability, and separation of concerns.

7. **Mock Data Fallback**: Mock data allows the frontend to remain fully demonstrable even when the backend is unavailable.

8. **No API Gateway**: Each service independently handles authentication validation, reducing architectural complexity and simplifying deployment.






---



## Feature Deep-Dives

### GIS Map Dashboard

The interactive map provides **real-time spatial awareness** of all deployed field assets:

- **OpenStreetMap tiles** rendered via React Leaflet
- **Color-coded sensor markers** driven by live alert severity
- **Animated pulse rings** on sensors with active alerts — drawing immediate operator attention
- **Sensor search autocomplete** with smooth fly-to animation on selection
- **Per-sensor detail drawer** with historical telemetry charts (1h / 24h / 7d / 30d time ranges)
- **Mock data fallback** the dashboard is fully demonstrable without backend connectivity

### Analytics Dashboard

A comprehensive operational intelligence view:

- **System Health Score** — circular gauge showing overall fleet health (0–100)
- **Battery Distribution Chart** — bar chart showing charge level across all sensors
- **Reading Occurrence Timeline** — scatter plot revealing sensor activity patterns
- **Threshold Breakdown Donut** — proportion of sensors in each severity band
- **Searchable Sensor Table** — filterable and sortable, with per-row trend drawer
- **Auto-refresh every 30 seconds** — always showing the latest state without manual reload

### Alert Engine

The alerting service implements a **4-level hierarchical severity model**, evaluated every minute using a sliding 10-minute window:

| Behaviour | Description |
|-----------|-------------|
| **Auto-create** | New alert raised when threshold is first crossed |
| **Escalation** | Severity upgraded if conditions worsen |
| **De-escalation** | Severity downgraded if conditions improve |
| **Auto-resolve** | Alert closed automatically when sensor returns to normal |
| **Retention** | Resolved alerts older than 1 day are pruned |

### Security Architecture

```mermaid
graph LR
    C[Client Browser] -->|1 - Login| US[User Service :8096]
    US -->|2 - JWT 15min + Refresh 1day| C
    C -->|3 - Bearer token| MS[Metadata/GIS Services]
    MS -->|4 - Validate JWT| JS[JwtService]
    C -->|5 - Refresh on 401| US
    US -->|6 - Check blacklist| REDIS[(Redis)]
    C -->|7 - Logout| US
    US -->|8 - Blacklist both tokens| REDIS
```

| Security Property | Implementation |
|-------------------|----------------|
| Short-lived access tokens | 15-minute JWT — limits blast radius of token theft |
| HttpOnly refresh cookie | Inaccessible to JavaScript — XSS-safe |
| Redis token blacklist | Immediate revocation on logout or token rotation |
| Role-Based Access Control | `ADMIN` and `USER` roles — gated at both frontend and backend |
| Auto token refresh | Axios interceptors transparently refresh tokens on `401` |


### Database Design

All services share the **`kernelx`** TimescaleDB database. Several tables are initialized as **hypertables**, thus automatically partitioned by time for high-throughput time-series queries.

- PostgreSQL relational database  
- Stores:
  - Asset metadata  
  - Historical records  
  - System configurations  



---


## End Product

### Testing

### Backend Testing
- **Unit & Integration tests** via JUnit 5 and Testcontainers (Alerting Service)
- **API endpoint testing** with Postman — validating CRUD operations, data validation, error handling, and JWT-protected routes

### Frontend Testing
- **UI testing** in browser — verifying API integration, data rendering, and user interactions
- **Mock data fallback** — ensures all pages load and function without backend dependencies

### Results
- ✅ Core functionalities operate correctly end-to-end
- ✅ Alert engine correctly creates, escalates, and resolves alerts
- ✅ JWT lifecycle (login → refresh → logout) operates with Redis blacklisting
- ✅ PDF report generation produces correct downloadable files
- ✅ System maintains data consistency across services



### Deployment Options

| Method | Best For | Command |
|--------|----------|---------|
| **Docker Compose** | Quick start, development, demo | `docker compose up --build -d` |
| **Manual / Dev Mode** | Active development of individual services | `./mvnw spring-boot:run` + `npm run dev` |
| **AWS EC2 + RDS** | Cloud production | See [DEPLOYMENT.md](DEPLOYMENT.md) |
| **Docker Swarm** | On-premise distributed | `docker stack deploy -c docker-compose.yml atlas` |
| **GKE / Kubernetes** | Enterprise-scale | Community contribution — see discussions |

---




## Conclusion

ATLAS successfully demonstrates a **scalable, modular, and domain-independent monitoring platform** suitable for multiple government applications.

### Achievements
- Developed a microservices-based full-stack system  
- Implemented real-time data ingestion using MQTT  
- Built a flexible and reusable architecture  
- GIS-based dashboard integration  
- Role-based authentication and security  
- Advanced alerting and notification system  
- Reporting and analytics services  


### Commercialization Potential
- Adaptable across multiple government sectors  
- Scalable for large-scale deployments  
- Suitable for smart city and infrastructure monitoring systems 

### Potential Future Developments

> **v1.0.0** is released and stable. Planned for future versions:

- [ ] **WebSocket push notifications** — eliminate polling, push alerts to clients in real-time
- [ ] **API Gateway** — centralized routing via Nginx / Spring Cloud Gateway
- [ ] **Kubernetes manifests** — Helm chart for enterprise deployments
- [ ] **TimescaleDB continuous aggregates** — efficient long-term analytics
- [ ] **Email / SMS alert notifications** — PagerDuty / Twilio integrations
- [ ] **Multi-language (i18n)** dashboard support
- [ ] **Prometheus + Grafana** metrics stack




<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f4c75,50:1b6ca8,100:0f4c75&height=100&section=footer" width="100%" />

*Built by Team KernelX · Department of Computer Engineering · University of Peradeniya*

</div>



<div align="center">

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/cepdnaclk/e22-co2060-hydro-risk-management)
[![Project Page](https://img.shields.io/badge/Project-Page-0f4c75?style=for-the-badge&logo=github-pages&logoColor=white)](https://cepdnaclk.github.io/e22-co2060-hydro-risk-management/)
[![Department](https://img.shields.io/badge/Computer_Engineering-UoP-8B0000?style=for-the-badge)](http://www.ce.pdn.ac.lk/)
[![University](https://img.shields.io/badge/University_of_Peradeniya-Sri_Lanka-006400?style=for-the-badge)](https://eng.pdn.ac.lk/)

</div>



[//]: # (Markdown reference: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
