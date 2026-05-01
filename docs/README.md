---
layout: home
permalink: index.html

# Please update this with your repository name and project title
repository-name: e22-co2060-hydro-risk-management
title: ATLAS – Adaptive Time-Series Analytics and Logging System
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template, and add more information required for your own project"

<!-- Once you fill the index.json file inside /docs/data, please make sure the syntax is correct. (You can use this tool to identify syntax errors)

Please include the "correct" email address of your supervisors. (You can find them from https://people.ce.pdn.ac.lk/ )

Please include an appropriate cover page image ( cover_page.jpg ) and a thumbnail image ( thumbnail.jpg ) in the same folder as the index.json (i.e., /docs/data ). The cover page image must be cropped to 940×352 and the thumbnail image must be cropped to 640×360 . Use https://croppola.com/ for cropping and https://squoosh.app/ to reduce the file size.

If your followed all the given instructions correctly, your repository will be automatically added to the department's project web site (Update daily)

A HTML template integrated with the given GitHub repository templates, based on github.com/cepdnaclk/eYY-project-theme . If you like to remove this default theme and make your own web page, you can remove the file, docs/_config.yml and create the site using HTML. -->

# ATLAS – Adaptive Time-Series Analytics and Logging System  
### Domain-Agnostic Government Monitoring Platform

---

## Team

-  E/22/182, Dinith Kariyawasam, [e22182@eng.pdn.ac.lk](mailto:e22182@eng.pdn.ac.lk)
-  E/22/291, Rameesha Prathapasinghe, [e22291@eng.pdn.ac.lk](mailto:e22182@eng.pdn.ac.lk)
-  E/22/421, Tharindu Weerasinghe, [e22421@eng.pdn.ac.lk](mailto:e22182@eng.pdn.ac.lk)
-  E/22/449, Gayumi Wimalaweera, [e22449@eng.pdn.ac.lk](mailto:e22182@eng.pdn.ac.lk)

<!-- Image (photo/drawing of the final hardware) should be here -->

<!-- This is a sample image, to show how to add images to your page. To learn more options, please refer [this](https://projects.ce.pdn.ac.lk/docs/faq/how-to-add-an-image/) -->

<!-- ![Sample Image](./images/sample.png) -->

#### Table of Contents
1. [Introduction](#introduction)
2. [Solution Architecture](#solution-architecture )
3. [Software Designs](#hardware-and-software-designs)
4. [Testing](#testing)
5. [Conclusion](#conclusion)
6. [Links](#links)

## Introduction

**ATLAS (Adaptive Time-Series Analytics and Logging System)** is a **domain-agnostic monitoring and management platform** designed to be adapted by multiple government organizations.

While the primary use case is **Integrated Hydro Risk Management**, the system is architected to support any domain requiring:

- Real-time measurements from field assets  
- Historical data analytics  
- Asset and infrastructure management  
- Scalable monitoring and reporting systems  

ATLAS enables:

- Real-time and periodic data collection  
- Centralized logging and storage of time-series data  
- Efficient asset and metadata management  
- Scalable and modular system expansion  

The platform can be extended to multiple domains such as:

- Irrigation systems  
- Power distribution  
- Environmental monitoring  
- Public infrastructure  
- Transportation systems  
- Smart city applications  

---


## Solution Architecture

The system is designed using a **microservices-based architecture** to ensure scalability, modularity, and flexibility.

### Key Components

- **Frontend (React 19 + Vite)**  
  Provides interactive dashboards and visualization interfaces  

- **MQTT Data Ingestion Service**  
  Handles real-time, high-frequency sensor data streams  

- **Metadata Handling Service**  
  Manages core entities, configurations, and historical data  

- **Alerting Service**  
  Performs risk analysis and generates alerts *(partially implemented)*  

- **Authentication Service (RBAC)**  
  Provides secure login and role-based access control *(to be implemented)*  

- **Reporting Service**  
  Generates reports and summaries from historical data *(to be implemented)*  

- **Database (PostgreSQL)**  
  Stores metadata, configurations, and historical records  



### System Flow

<pre>
Sensors / External Sources
            ↓
MQTT Data Ingestion Service
            ↓
   Backend Microservices
            ↓
         Database
            ↓
    Frontend Dashboard
</pre>

---
## Software Designs

### Frontend Design
- Built using **React with Vite**  
- Component-based architecture  
- Handles dashboards, alerts, and user interactions  



### Backend Design
- Implemented using **Spring Boot and Node.js microservices**  
- RESTful API architecture  
- Loosely coupled services for scalability  



### Database Design
- PostgreSQL relational database  
- Stores:
  - Asset metadata  
  - Historical records  
  - System configurations  



### Key Features

- Real-time alerts and monitoring dashboard  
- MQTT-based automated data ingestion  
- Full CRUD metadata management  
- Modular microservices architecture  

---

## Testing

### Backend Testing
- API endpoints tested using Postman  
- Verified:
  - CRUD operations  
  - Data validation  
  - Error handling  



### Frontend Testing
- UI tested in browser  
- Verified:
  - Data rendering  
  - API integration  
  - User interaction  

---

### Results Summary
- Core functionalities operate correctly  
- System maintains data consistency  
- Errors are handled appropriately  
- Platform is stable under normal conditions  

---


## Conclusion

ATLAS successfully demonstrates a **scalable, modular, and domain-independent monitoring platform** suitable for multiple government applications.

### Achievements
- Developed a microservices-based full-stack system  
- Implemented real-time data ingestion using MQTT  
- Built a flexible and reusable architecture  



### Future Developments
- GIS-based dashboard integration  
- Role-based authentication and security  
- Advanced alerting and notification system  
- Reporting and analytics services  



### Commercialization Potential
- Adaptable across multiple government sectors  
- Scalable for large-scale deployments  
- Suitable for smart city and infrastructure monitoring systems  

---


## Links

- [Project Repository](https://github.com/cepdnaclk/e22-co2060-hydro-risk-management.git)
- [Project Page](https://github.com/cepdnaclk/e22-co2060-hydro-risk-management/blob/8bc0f329aeb7c6beade07b665331d8104fdc32e4/docs/README.md/)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

[//]: # (Please refer this to learn more about Markdown syntax)
[//]: # (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
