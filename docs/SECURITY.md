# 🔒 Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| `main` branch | ✅ Active development |
| Older releases | ❌ Not supported |

---

## 🚨 Reporting a Vulnerability

**Please do NOT report security vulnerabilities through public GitHub issues.**

If you discover a security vulnerability in ATLAS, please report it responsibly:

### Option 1 — GitHub Private Vulnerability Reporting (Preferred)

Use GitHub's built-in private vulnerability reporting:  
**[Report a vulnerability](https://github.com/cepdnaclk/e22-co2060-hydro-risk-management/security/advisories/new)**

### Option 2 — Email

Send details to: **e22182@eng.pdn.ac.lk**  
Include `[SECURITY]` in the subject line.

---

## 📋 What to Include in Your Report

To help us triage and fix the issue quickly, please include:

- **Description** of the vulnerability and its potential impact
- **Steps to reproduce** (proof-of-concept if possible)
- **Affected component** (which service, which endpoint)
- **Suggested fix** (if you have one)
- Your name/handle for acknowledgment (optional)

---

## ⏱️ Response Timeline

| Action | Timeline |
|--------|----------|
| Initial acknowledgment | Within 48 hours |
| Severity assessment | Within 5 business days |
| Fix or workaround | Depends on severity |
| Public disclosure | After fix is released |

We follow a **90-day responsible disclosure** policy. We will keep you informed throughout the process.

---

## ⚠️ Known Security Considerations

If you are deploying ATLAS in production, please be aware of these important points:

### 1. Change Default Credentials

The `DataSeeder` seeds a default admin account:
```
username: admin
password: admin123
```
**Change this immediately** by setting `ADMIN_PASSWORD` in your `.env` file.

### 2. Change the JWT Secret

The default JWT secret in the repository is for **development only**:
```
jwt.secret: 404E635266556A586E3272357538782F413F4428472B4B6250645367566B5970
```
Generate a secure secret for production:
```bash
openssl rand -hex 32
```

### 3. Database Credentials

The `docker-compose.yml` defaults to `kernelx/kernelx`. Use strong, unique credentials in production via the `.env` file.

### 4. MQTT Topic Security

The default MQTT setup uses the **public HiveMQ broker** (`broker.hivemq.com`). Anyone who knows your topic pattern can publish to it. For production:
- Use a **private MQTT broker** (Mosquitto, EMQX, AWS IoT)
- Enable **TLS** (use `ssl://` instead of `tcp://`)
- Configure **MQTT authentication** (username/password or client certificates)

### 5. No API Gateway

ATLAS does not include an API gateway or rate limiting by default. For internet-facing deployments, consider placing a reverse proxy (Nginx, Traefik, AWS ALB) in front of all services.

---

## 🙏 Acknowledgments

We are grateful to security researchers who practice responsible disclosure. Verified vulnerability reporters will be acknowledged in our release notes (with your permission).
