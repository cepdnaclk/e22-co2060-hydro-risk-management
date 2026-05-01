# 🌊 Integrated Hydro Risk Management System
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-3C52F0?style=for-the-badge&logo=mqtt&logoColor=white)
<p align="center">
  <img width="800" height="500" alt="readme image" src="https://github.com/user-attachments/assets/e8e19beb-3360-48b2-b968-06bea651055e" />
</p>

**ATLAS** is a domain‑agnostic monitoring and management platform designed to be adapted by multiple government organizations. While the primary use case is **Integrated Hydro Risk Management**, the system is architected to support any domain requiring real-time measurements, historical analytics, and asset management.

## ✨ Core Features
  * **Real-time Alerts**: A modern, responsive interface for visualizing risk alerts and   monitoring trends.
  * **Automated Data Ingestion**: Seamless MQTT-based processing of field sensor data.
  * **Metadata Management**: Full CRUD interfaces to manage disaster-related entities and configurations.
  * **Microservices Architecture**: Decoupled backend services designed for modularity and scalability.
    ## To be implemented
  * **GIS‑Based Dashboard**: Integrated mapping for spatial awareness and real-time visualization of distributed field assets.
  * **Role-Based Access & Secure Login**: Robust authentication and authorization to ensure data security across different administrative levels.
  * **Reporting Service**: Automated generation of periodic reports and data summaries for decision-makers.

## 🏗️ System Architecture
The system is divided into several specialized modules:
1. **Frontend**: Built with React 19 and Vite for the monitoring dashboard.
2. **MQTT Ingestion Service**: Processes high-frequency data streams from remote sensors.
3. **Metadata Handling Service**: Manages core entities, historical records, and configurations.
4. **Alerting Service**: Logic engine for risk assessment and notification broadcasting.

## 👥 Team Members (Group 37)
```text
  * Dinith Kariyawasam (E/22/182)
      -e22182@eng.pdn.ac.lk
  * Rameesha Prathapasinghe (E/22/291)
      -e22291@eng.pdn.ac.lk
  * Tharindu Weerasinghe (E/22/421)
      -e22421@eng.pdn.ac.lk
  * Gayumi Wimalaweera (E/22/449)
      -e22449@eng.pdn.ac.lk

**Supervised by: Prof.Kamalanath Samarakoon**
```

## 📂 Project Structure
```Plaintext
e22-co2060-hydro-risk-management/
├── code/                                          # Centralized source code
│   ├── disaster-management-alerting-service/           # Notification & Alert logic
│   ├── metadata-handling-service/                      # Core entity & Data API
│   ├── mqtt-data-ingestion-service/                    # Sensor data processing
│   └── [disaster-management-frontend]/                 # React dashboard (if added here)
├── docs/                                          # GitHub Pages & Portal Metadata
│   ├── index.json                                 # Team & Project info for portal
│   └── _config.yml                                # Page theme settings
├── additional-files/                              # Research & Requirements
├── docker-compose.yml                             # (Reserved for future orchestration)
└── README.md                                      # Project overview
```
## 📜 License
Licensed under the [MIT License](LICENSE). Created for the CO2060 Software Systems Design module, Department of Computer Engineering, University of Peradeniya.
