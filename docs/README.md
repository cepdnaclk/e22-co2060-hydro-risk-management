---
layout: home
permalink: index.html
repository-name: e22-co2060-hydro-risk-management
title: ATLAS – Adaptive Time-Series Analytics and Logging System
---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f4c75,50:1b6ca8,100:0f4c75&height=220&section=header&text=ATLAS&fontSize=80&fontColor=ffffff&fontAlignY=38&desc=Adaptive%20Time-Series%20Analytics%20and%20Logging%20System&descAlignY=62&descSize=20&animation=fadeIn" width="100%" alt="ATLAS — Adaptive Time-Series Analytics and Logging System" />
<img width="100%" alt="Image" src="https://github.com/user-attachments/assets/f277d23a-83e9-402c-bb13-f0f0df324c28" />

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


### Table of Contents
1. [Introduction](#introduction)
2. [Live Dashboard Preview](#live-dashboard-preview)
3. [System Design](#system-design)
4. [System Architecture](#system-architecture)
5. [Feature Deep-Dives](#feature-deep-dives)
6. [End Product](#end-product)
7. [Conclusion](#conclusion)


---

## Introduction

**ATLAS (Adaptive Time-Series Analytics and Logging System)** is a **domain-agnostic monitoring and management platform** designed to be adapted by multiple government organizations.

While the primary use case is *Integrated Hydro Risk Management*, the system is architected to support any domain requiring:

- Real-time measurements from field assets  
- Historical data analytics  
- Asset and infrastructure management  
- Scalable monitoring and reporting systems  

The platform connects 
**IoT field sensors → MQTT message broker → intelligent backend services → interactive GIS dashboard**,
delivering a complete real-time situational awareness system for decision-makers and field operators.

ATLAS enables:

- Real-time and periodic data collection  
- Centralized logging and storage of time-series data  
- Efficient asset and metadata management  
- Scalable and modular system expansion  

The **ATLAS (Adaptive Time-Series Analytics and Logging System)** is a full-stack, microservices-based monitoring platform engineered for "Integrated Hydro Risk Management": with the architectural flexibility to serve any domain
 involving field sensors, real-time data, and risk alerting platform.

*Domains ATLAS can serve out-of-the-box using different sensor sets:*

- **🌊 Hydro Risk Flood / drought alerts** : Water level, Rainfall, Flow rate
- **💧 Irrigation Water stress / overflow** : Soil moisture, Tank level, Flow
- **🌿 Environment  Pollution thresholds** : Air quality, CO2, PM2.5, Temperature
- **⚡ Power Grid outage / overload risk** : Voltage, Current, Load
- **🏙️ Smart City congestion / comfort** : Traffic density, Noise, Humidity
- **🏭 Industrial equipment fault detection** : Pressure, Vibration, Temperature


> Originally developed as the primary use case for *flood and hydrological risk monitoring* across Sri Lankan river systems, ATLAS is built to scale seamlessly into irrigation networks, power distribution, environmental monitoring, and smart city infrastructure.



---


## Live Dashboard Preview

<div align="center">

<p align="center">
  <img
    src="https://github.com/cepdnaclk/e22-co2060-hydro-risk-management/blob/main/docs/images/ATLAS_Dashboard.gif"
    alt="Hydro Risk Management Project Demo"
    width="90%"
  />
</p>

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

[![](https://mermaid.ink/img/pako:eNp9Vdtu2zgQ_ZWBFoFTVE5syzfpoYAdy1lh0zSJ3TwsDCwoaWwTkUiXpNx4Db_uB_QT-yU7lCxvtvWuHiSKc-Zw5gw53DuJTNEJnIuLPRfcBLBvmDXm2AgaMdPYcKvfZ6Y4izPUjWDfWEphpizn2Y5QkTCoXJjhSiJ8jlzQTOimRsWX5MwSI9X4ZUXAX9IY2RJPk1KlqOx8p9f3MK7n5_hqbmQmS1MbPTZkZBLSINGcDEtcesmgNpRUJ1vqDwatPtk0XwmWnea7g16v7zcOh8PFxUIthMYvBYoEJ5ytFMvtFNDDCiNFkceo6pkNU4YnfMOEoTyFlgqYhinHLD3-n0N-fJzPLa78jpV8OU8YiRVqY4HViEtBpGrLEzwHn4wtdM5z1AnLcDI-BxplqErKahCKFRdn2aahRU2YXseSqdRCapjCxIBaxZedbsuFTs-jV7f7rjbfk-4gt6iOCriTcQDR_W04m0ef7uEhegjvovuwhleg5ocPVo0AHoo443oN-xRtolHqwpZlBbpgbGaG5RsXYmZoa-0ONYd1JYZKpgBmRawTxWMEEiKLWfICl49yBu1TjBXyjcszy3jKKPD3EBfLJQXPBdxIkRRKoTCPBRb4c4K195iZZA3LrKDAkQw7GILGRIpU_7SiVUOzLY6y7DK2fu_g-1_f3tYN1rsNFcceqtobxX9UoNe14nfK15kKlFUuCzC6C5_mED6P7j6PbB1qbCblBsIy5jbkXBTkepkoKU5s9il5jsGTFgTWZdn-UMhSLlbaypUx2q3tVpNY4CsXqfx6jqL8BqRtTtsNycnYTX7kga0-MoNZK9Rrmf0j4Y-B3JATRXsNoRWuGj6hltkWgVmc_kG-_1fSOyk5PKPkNCxlvIueQ5iMZr-OP42eJnBpW0JT4dLGCl5Lnzyn4THK23AO11VO2oVrgxk1TaN211XmTdqhNF3Fe019jm9PVZ-Mm0QyDQNKyxSKFCZjrc_7KkegXcv-tWiFF9T34DaaQc7owCRrOtq0_G8PEZ0Jlb5VxnGdleKpEyxZptF1clQ5s__O3mIWTtnmF05AQ4Vp8dpMbN9cOAtxIF_qFr9LmTuBUXRKHSWL1frEVWzsoTq20ROkDO5GFsI4QcdvlRxOsHdenaDZbrWuBr1O3_fagz59qCzOjmD9K7_bavUHHb_d6fmDfv_gOn-W67au_GHX6_nesO35_tDr-66DKacL42N1gZX32OFv2DEx_w?type=png)](https://mermaid.live/edit#pako:eNp9Vdtu20YQ_ZUBC0MKQln3Gx8CSBblEnUc21L8UAgoluRIWpjcVXaXilVBr_2AfGK-pLOkyLqJWj6Qy5kzhzNndodHJ5IxOp5zdXXkghsPjjWzxRRrXi1kGmtu8frMFGdhgrrmHWtrKcycpTw5ECoQBpULC9xIhM-BC5oJ3dCo-JqCWWSkmr5sCPhLHCJbY2WUKkZl7Z3-oIthaV_iq7mRicxdbeyyESOXkAaJpnKscd2NhqUjp6p88Xg4bA3Ip_lGsKSy94b9_mBcO51OV1crtRIav2QoIpxxtlEstSagi2VGiiwNUZWWHVOGR3zHhKE6hZYKmIY5xyQ-v19CfnxcLi0uf06VfLlMGIgNamOBxYpLQaRqzyO8BJ9NLXTJU9QRS3A2vQSaJKhyymLhiw0XF9nmvkXNmN6GkqnYQkqYwsiA2oT1Tq_lQqffpVuv965035PuIPeozgq4s6kHwf2tv1gGn-7hIXjw74J7v4QXoMaHD1YNDx6yMOF6C8cYbaFB7MKeJRm6YGxlhqU7F0JmaGsdTiWHDSWGQiYPFlmoI8VDBBIiCVn0AvVHuYB2lWOBfBPyzBIeM0r8PYTZek3JcwE3UkSZUijMY4YZ_lxgGT1lJtrCOskocSTHAUagMZIi1j990aqh2R4nSVIPbdw7-P7Xt7d9g-1hR82xh6qMRvEfHej3rPid_HahA3mX8wZM7vynJfjPk7vPE9uHEptIuQM_z7kNKRcZhdYjJUXFZq-c55w8aUFgnbftD4Us5mKjrVwJo93abjWIBb5yEcuvlyjyp0faprTdkIKM3eRnHtjrMzOYrUK9lck_Ev6YyA0FUbZN8K1wxfIJtUz2CMzi9A_y_b-S3UrJ0QUl534u413w7MNssvh1-mnyNIO6HQkNhWubK3Rbuoqc--csb_0lNIuatAtNgwkNTaMOzaLyBu1QMhf5NmnO8X3V9dm0QSRz36OyTKZIYXKW-rwvagTatexfHy3wguYe3AYLSBkdmGhLR5s-_9tDQGdCxW-VcVxno3jseGuWaHSdFFXK7LtztJiVk4_5lePRUmGcvTYiOzdXzkqcKJamxe9Spo5nFJ1SR8lss624sp09VOcxWllVnt2NzIRxvM6on5M43tF5dbxGu9W6HvY7g3G3PRzQg_riHAg2uB73Wq3BsDNud_rj4WBwcp0_8w-3rsejXrc_7o7ao_G41-kNXAdjTn-Mj8UfLP-Rnf4GDvQySQ)



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

<div align="center">
<img width="80%" alt="ATLAS System Architecture Diagram" src="https://github.com/user-attachments/assets/1884f50b-6fda-4d0f-bcaa-345aff1569db" />

<br>

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
<br>

### GIS Map Dashboard

The interactive map provides **real-time spatial awareness** of all deployed field assets:

- **OpenStreetMap tiles** rendered via React Leaflet
- **Color-coded sensor markers** driven by live alert severity
- **Animated pulse rings** on sensors with active alerts — drawing immediate operator attention
- **Sensor search autocomplete** with smooth fly-to animation on selection
- **Per-sensor detail drawer** with historical telemetry charts (1h / 24h / 7d / 30d time ranges)
- **Mock data fallback** the dashboard is fully demonstrable without backend connectivity
<br>

### Analytics Dashboard

A comprehensive operational intelligence view:

- **System Health Score** — circular gauge showing overall fleet health (0–100)
- **Battery Distribution Chart** — bar chart showing charge level across all sensors
- **Reading Occurrence Timeline** — scatter plot revealing sensor activity patterns
- **Threshold Breakdown Donut** — proportion of sensors in each severity band
- **Searchable Sensor Table** — filterable and sortable, with per-row trend drawer
- **Auto-refresh every 30 seconds** — always showing the latest state without manual reload
<br>

### Alert Engine

The alerting service implements a **4-level hierarchical severity model**, evaluated every minute using a sliding 10-minute window:

- **Auto-create** - New alert raised when threshold is first crossed 
- **Escalation** - Severity upgraded if conditions worsen 
- **De-escalation** - Severity downgraded if conditions improve 
- **Auto-resolve** - Alert closed automatically when sensor returns to normal 
- **Retention** - Resolved alerts older than 1 day are pruned 

<br>

### Security Architecture


[![](https://mermaid.ink/img/pako:eNqNVdtu2zgQ_RWCARY1aqe631AUSByjTRG3gRV3ga36QFNDW4gspRS1STbJd-37ftkOJUuOHQetHixZPHPOmRly9EB5mQKNqMjLW75iUpGLWSKTguBV1YulZDcrMr44n3y5-p7QcZ5BgRB2DzKhPzqgvsbb5VNZ3lY7AChS_fiC-GR-9QnjTmq1wsCMM5WVBfnvXzLHeBKD_DvjsCc0jzHi-fr7hXz34bJE64ERenvoz39q3_i7g74qr6Eg31iepY3kb1iNJ7Nv5-OJFr-UpQKuIO04qz3RqUZNQTFkZ-Qd-XgeH4K-KnX1dXbycYIcMVSVrsgfpHUcK6b26zGbnJ3H398kdAZpVj1L7zRn_DrPKpXQwWuaYzIafXhM6BtzQC7KZVYQLiHVvWA5Wn3EanfQedxhrQE54ZhKpauru2W6ZJ0VjfQMhIRqRVRjQa-RlN1rpvFBXXtAToFJ7GYToYHTXnLaSzqDrlugRTVM3zY4bWN03CC3PSXoo87VlvGFtjsgnV0mFFpwDPO1nL0BGa-AX28SW2xr-9h24KCC31S1rBWa-VlDCz9EHwy27SKsLe5bDHpWzOqgFM9ZVZ2BwIfm7Iksz6OjdAFMwLBSEiOjI8v1bFgMeZmXMjoywWYB2yyObrNUrSLr5u4FI8NT2fFxwcHv-UyP2Q7r-RzXttJf81XtCdhQChsCIXrK0LZt6CndwOSB_xuUqpRs2VMKSFO3pwTmBgbvKEO0bFoHKXdosXltKXffzuOh3mW6JrsLuEc3ie2-bzrVGdw55uo-h81I3RgHIbydWnBX7BXU3GbfEujR2eVtiFQ4fXjggWD8F-HdOOsomHCfOUiDhdPvn1cp2jHVF1_4kPYMIl0w33nBQId0KbOURgLnCwzpGuSa6f_0QVMnFD8Ea5xwET7iIKrvRk37EpoUTxh7w4q_ynJNIyVrjJZlvVz1XPWNHg9nGcMpuoXgwAM5LutC0cgK3IaDRg_0jkYj0zCOfdfyQtv0Pby59pDeI8w7Dh3D8HwrNC039D3vaUj_aXSN4zBwbDe0AzMIQ8dyvCHFsYtdnrbf0eZz-vQ_9Jpbjg?type=png)](https://mermaid.live/edit#pako:eNqNVdtu2zgQ_RWCARY1aqe631AUSByjTRG3gRV3ga36QFNDW4gspRS1STbJd-37ftkOJUuOHQetHixZPHPOmRly9EB5mQKNqMjLW75iUpGLWSKTguBV1YulZDcrMr44n3y5-p7QcZ5BgRB2DzKhPzqgvsbb5VNZ3lY7AChS_fiC-GR-9QnjTmq1wsCMM5WVBfnvXzLHeBKD_DvjsCc0jzHi-fr7hXz34bJE64ERenvoz39q3_i7g74qr6Eg31iepY3kb1iNJ7Nv5-OJFr-UpQKuIO04qz3RqUZNQTFkZ-Qd-XgeH4K-KnX1dXbycYIcMVSVrsgfpHUcK6b26zGbnJ3H398kdAZpVj1L7zRn_DrPKpXQwWuaYzIafXhM6BtzQC7KZVYQLiHVvWA5Wn3EanfQedxhrQE54ZhKpauru2W6ZJ0VjfQMhIRqRVRjQa-RlN1rpvFBXXtAToFJ7GYToYHTXnLaSzqDrlugRTVM3zY4bWN03CC3PSXoo87VlvGFtjsgnV0mFFpwDPO1nL0BGa-AX28SW2xr-9h24KCC31S1rBWa-VlDCz9EHwy27SKsLe5bDHpWzOqgFM9ZVZ2BwIfm7Iksz6OjdAFMwLBSEiOjI8v1bFgMeZmXMjoywWYB2yyObrNUrSLr5u4FI8NT2fFxwcHv-UyP2Q7r-RzXttJf81XtCdhQChsCIXrK0LZt6CndwOSB_xuUqpRs2VMKSFO3pwTmBgbvKEO0bFoHKXdosXltKXffzuOh3mW6JrsLuEc3ie2-bzrVGdw55uo-h81I3RgHIbydWnBX7BXU3GbfEujR2eVtiFQ4fXjggWD8F-HdOOsomHCfOUiDhdPvn1cp2jHVF1_4kPYMIl0w33nBQId0KbOURgLnCwzpGuSa6f_0QVMnFD8Ea5xwET7iIKrvRk37EpoUTxh7w4q_ynJNIyVrjJZlvVz1XPWNHg9nGcMpuoXgwAM5LutC0cgKzIaDRg_0jkYj0zCOfdfyQtv0Pby59pDeI8w7Dh3D8HwrNC039D3vaUj_aXSN4zBwbDe0AzMIQ8dyvCHFsYtdnrbf0eZz-vQ_8v5big)


Security properties and method of implementations are as below:

- **Short-lived access tokens** - 15-minute JWT (limits blast radius of token theft)
- **HttpOnly refresh cookie** - Inaccessible to JavaScript (XSS-safe)
- **Redis token blacklist** - Immediate revocation on logout or token rotation
- **Role-Based Access Control** - `ADMIN` and `USER` roles gated at both frontend and backend
- **Auto token refresh** - Axios interceptors transparently refresh tokens on `401`

<br>

### Database Design

All services share the **`kernelx`** TimescaleDB database. Several tables are initialized as **hypertables**, thus automatically partitioned by time for high-throughput time-series queries.

- PostgreSQL relational database  
- Stores:
  - Asset metadata  
  - Historical records  
  - System configurations  



---

## End Product

<br>

### Testing

- Backend Testing
  - **Unit & Integration tests** via JUnit 5 and Testcontainers (Alerting Service)
  - **API endpoint testing** with Postman — validating CRUD operations, data validation, error handling, and JWT-protected routes

- Frontend Testing
  - **UI testing** in browser — verifying API integration, data rendering, and user interactions
  - **Mock data fallback** — ensures all pages load and function without backend dependencies

- Results
  - ✅ Core functionalities operate correctly end-to-end
  - ✅ Alert engine correctly creates, escalates, and resolves alerts
  - ✅ JWT lifecycle (login → refresh → logout) operates with Redis blacklisting
  - ✅ PDF report generation produces correct downloadable files
  - ✅ System maintains data consistency across services



### Deployment Options


- For Quick start, development, demo:
  - **Docker Compose** :`docker compose up --build -d`

- Active development of individual services
  - **Manual / Dev Mode** : `./mvnw spring-boot:run` + `npm run dev`

- Cloud production
  - **AWS EC2 + RDS** : See [DEPLOYMENT.md](DEPLOYMENT.md)
  
- On-premise distributed
  - **Docker Swarm** : `docker stack deploy -c docker-compose.yml atlas`

- Enterprise-scale
  - **GKE / Kubernetes** : Community contribution (see discussions)


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

- [ ] *WebSocket push notifications* — eliminate polling, push alerts to clients in real-time
- [ ] *API Gateway* — centralized routing via Nginx / Spring Cloud Gateway
- [ ] *Kubernetes manifests* — Helm chart for enterprise deployments
- [ ] *TimescaleDB continuous aggregates* — efficient long-term analytics
- [ ] *Email / SMS alert notifications* — PagerDuty / Twilio integrations
- [ ] *Multi-language (i18n)* dashboard support
- [ ] *Prometheus + Grafana* metrics stack




<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f4c75,50:1b6ca8,100:0f4c75&height=100&section=footer" width="100%" />

*Built by Team KernelX · Department of Computer Engineering · University of Peradeniya*

</div>



<div align="center">

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-64748B?style=for-the-badge&logo=github)](https://github.com/cepdnaclk/e22-co2060-hydro-risk-management)
[![Project Page](https://img.shields.io/badge/Project-Page-11669e?style=for-the-badge&logo=github-pages&logoColor=white)](https://cepdnaclk.github.io/e22-co2060-hydro-risk-management/)
[![Department](https://img.shields.io/badge/Computer_Engineering-UoP-bd0000?style=for-the-badge)](http://www.ce.pdn.ac.lk/)
[![University](https://img.shields.io/badge/University_of_Peradeniya-Sri_Lanka-09b309?style=for-the-badge)](https://eng.pdn.ac.lk/)

</div>



[//]: # (Markdown reference: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
