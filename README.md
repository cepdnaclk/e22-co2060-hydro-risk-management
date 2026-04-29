#🌊 Integrated Hydro Risk Management System

A comprehensive, microservice-based platform designed for real-time monitoring, analysis, and mitigation of hydrological risks. This system provides disaster management authorities with actionable insights through automated sensor data ingestion, metadata management, and predictive alerting.

✨ Core Features
1. Real-time Alerts Dashboard: A modern, responsive interface for visualizing risk alerts and monitoring trends.
2. Automated Data Ingestion: Seamless MQTT-based processing of field sensor data.
3. Metadata Management: Full CRUD interfaces to manage disaster-related entities and configurations.
4. Microservices Architecture: Decoupled backend services designed for modularity and scalability.

🏗️ System Architecture
The system is divided into several specialized modules:
1. Frontend: Built with React 19 and Vite for the monitoring dashboard.
2. MQTT Ingestion Service: Processes high-frequency data streams from remote sensors.
3. Metadata Handling Service: Manages core entities, historical records, and configurations.
4. Alerting Service: Logic engine for risk assessment and notification broadcasting.

🚀 Getting Started
Prerequisites
Make sure you have the following installed:
  * Node.js (v18.0.0 or higher)
  * JDK 17+ & Maven
  * MQTT Broker (e.g., Mosquitto)

Local Installation
Clone the repository:Bashgit clone <repository-url>
Run Backend Services: Navigate to each service folder in /code and run:Bashmvn spring-boot:run
Run Frontend: ```bashcd code/disaster-management-frontendnpm installnpm run dev

👥 Team Members (Group 37)
  * Dinith Kariyawasam (E/22/182)
      -e22182@eng.pdn.ac.lk
  * Rameesha Prathapasinghe (E/22/291)
      -e22291@eng.pdn.ac.lk
  * Tharindu Weerasinghe (E/22/421)
      -e22421@eng.pdn.ac.lk
  * Gayumi Wimalaweera (E/22/449)
      -e22449@eng.pdn.ac.lk
Supervised by: Prof.Kamalanath Samarakoon

📂 Project StructurePlaintexthydro-risk-management/
├── code/                               # Source code for all microservices
├── docs/                               # GitHub Pages & Project Portal Metadata
│   ├── index.json                      # Portal configuration (Team info)
│   └── _config.yml                     # Page theme settings
├── additional-files/                   # Research & Specifications
└── README.md

📜 License
Licensed under the MIT License. Created for the CO2060 Software Systems Design module, Department of Computer Engineering, University of Peradeniya.
