# 🌊 Integrated Hydro Risk Management System
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-3C52F0?style=for-the-badge&logo=mqtt&logoColor=white)

<img width="1000" height="500" alt="Image" src="https://github.com/user-attachments/assets/1313d9bf-c826-44d0-a745-d6c4180fd1f6" />

A comprehensive, microservice-based platform designed for real-time monitoring, analysis, and mitigation of hydrological risks. This system provides disaster management authorities with actionable insights through automated sensor data ingestion, metadata management, and predictive alerting.

## ✨ Core Features
1. **Real-time Alerts Dashboard**: A modern, responsive interface for visualizing risk alerts and   monitoring trends.
2. **Automated Data Ingestion**: Seamless MQTT-based processing of field sensor data.
3. **Metadata Management**: Full CRUD interfaces to manage disaster-related entities and configurations.
4. **Microservices Architecture**: Decoupled backend services designed for modularity and scalability.

## 🏗️ System Architecture
The system is divided into several specialized modules:
1. **Frontend**: Built with React 19 and Vite for the monitoring dashboard.
2. **MQTT Ingestion Service**: Processes high-frequency data streams from remote sensors.
3. **Metadata Handling Service**: Manages core entities, historical records, and configurations.
4. **Alerting Service**: Logic engine for risk assessment and notification broadcasting.

## 🚀 Getting Started
### **Prerequisites**
Make sure you have the following installed:
  * Node.js (v18.0.0 or higher)
  * JDK 17+ & Maven
  * MQTT Broker (e.g., Mosquitto)

**Local Installation**
1. **Clone the repository:**
```bash
git clone <repository-url>
```

3. **Run Backend Services:**
Navigate to each service folder in ```code/``` and run:
```bash
mvn spring-boot:run
```

5. **Run Frontend:**
```bash
cd code/disaster-management-frontend
npm install
npm run dev
```

## 👥 Team Members (Group 37)
  * Dinith Kariyawasam (E/22/182)
      -e22182@eng.pdn.ac.lk
  * Rameesha Prathapasinghe (E/22/291)
      -e22291@eng.pdn.ac.lk
  * Tharindu Weerasinghe (E/22/421)
      -e22421@eng.pdn.ac.lk
  * Gayumi Wimalaweera (E/22/449)
      -e22449@eng.pdn.ac.lk

**Supervised by: Prof.Kamalanath Samarakoon**

## 📂 Project Structure
```Plaintext
hydro-risk-management/
├── code/                               # Source code for all microservices
├── docs/                               # GitHub Pages & Project Portal Metadata
│   ├── index.json                      # Portal configuration (Team info)
│   └── _config.yml                     # Page theme settings
├── additional-files/                   # Research & Specifications
└── README.md
```
📜 License
Licensed under the MIT License. Created for the CO2060 Software Systems Design module, Department of Computer Engineering, University of Peradeniya.
