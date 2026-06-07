# HackerMind 🧠🔓

![Microsoft](https://img.shields.io/badge/Microsoft-Agents%20League%20Hackathon%202026-blue?style=flat)
![Track](https://img.shields.io/badge/Track-Creative%20Apps-purple?style=flat)
![Foundry IQ](https://img.shields.io/badge/Powered%20by-Foundry%20IQ-cyan?style=flat)
![Azure](https://img.shields.io/badge/Hosted%20on-Azure-blue?style=flat)
![Live Demo](https://img.shields.io/badge/Live-Demo-green?style=flat)
![GitHub Copilot](https://img.shields.io/badge/Built%20with-GitHub%20Copilot-black?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

> **Five AI agents. One target. Complete visibility.**

Cybersecurity threats don't announce themselves. They hide in plain sight — inside your APIs, your databases, your cloud configurations, your authentication flows. HackerMind tears them apart.

Describe any system. Five specialized AI agents — powered by Microsoft Foundry IQ (Azure OpenAI gpt-4.1-mini) — will dissect it from every angle: architecture mapping, vulnerability hunting, defense strategy, security reporting, and risk scoring. All in real time. All in one platform.

Built for Microsoft Agents League Hackathon 2026 — Creative Apps Track.

---

## 🎬 Demo

> 📹 [Watch the demo →](https://youtu.be/U24y8VNIywA?si=MEhkdV2BCKhSMgTX)

> 🌐 [Launch the live web app →](https://hackermind-rhea-dsasf9bfbba5h7hc.swedencentral-01.azurewebsites.net)
---

## 🤖 The Five Agents

HackerMind doesn't just call an AI — it orchestrates a **multi-agent reasoning pipeline** where each agent builds on the previous one's output.

| Agent | Role | What it does |
|-------|------|-------------|
| 🔍 **AGENT_ANALYZER** | System Cartographer | Maps the system architecture, identifies components, and defines the attack surface |
| ⚔️ **AGENT_ATTACKER** | Ethical Hacker | Thinks like an adversary — identifies every exploitable vulnerability and attack vector |
| 🛡️ **AGENT_DEFENDER** | Security Architect | For every vulnerability found, builds specific, actionable defense strategies |
| 📋 **AGENT_REPORTER** | Intelligence Officer | Synthesizes all findings into a structured, professional security report |
| 📊 **AGENT_SCORER** | Risk Quantifier | Scores six threat categories from 0-100 and calculates an overall risk index |

Each agent receives the output of the previous agent as context — creating a true reasoning chain, not just parallel API calls.

---

## ✨ Core Features

### 🧠 Multi-Agent Reasoning Pipeline — Microsoft Foundry IQ

Every analysis triggers a sequential five-agent chain powered by Microsoft Foundry IQ (Azure OpenAI gpt-4.1-mini). The pipeline runs end-to-end from a single system description — no manual intervention, no hardcoded responses.

The pipeline generates context-aware analyses tailored to each system description Every run is dynamically generated, context-aware, and grounded in real cybersecurity knowledge.

### 📊 Risk Intelligence Dashboard

Six threat dimensions scored in real time:

| Threat Category | What it measures |
|----------------|-----------------|
| **SQL Injection** | Input validation and query parameterization weaknesses |
| **XSS** | Cross-site scripting exposure across user-facing surfaces |
| **Auth Bypass** | Authentication and session management vulnerabilities |
| **API Security** | Endpoint exposure, rate limiting, and authorization gaps |
| **Data Exposure** | Sensitive data handling, encryption, and storage risks |
| **Network Attack** | Network-layer threats, open ports, and traffic interception risks |

### 🗺️ Interactive 3D Risk Map

A live, mouse-reactive 3D visualization of your system's vulnerability topology. Each node represents a system component — Web Server, API Gateway, Database, Cloud Infrastructure, Core System. Nodes glow red when critical vulnerabilities are detected, amber for warnings, green for healthy components. Click any node for a detailed diagnostic panel.

### 🔬 Defense Lab

A dedicated workspace showing AI-generated defense strategies with a real-time strategy scorecard. Resilience, Coverage, and Mitigation scores calculated dynamically from the analysis results. The Defensive Library surfaces relevant security controls and tools based on the threat profile.

### 💻 Cyberpunk Terminal UI

A fully immersive cyberpunk interface with:
- Animated scanline overlays
- Hologram glass panels with glow effects
- Live analyst feed with real-time threat intelligence updates
- Matrix-style grid background
- Terminal-style progress indicators during analysis

---

## 🏗️ Architecture
![HackerMind Architecture](Architecture%20Diagram.jpg)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | HTML, CSS, Vanilla JavaScript, Tailwind CSS |
| **Backend** | Python, Flask |
| **AI Engine** | Microsoft Foundry IQ — Azure OpenAI gpt-4.1-mini |
| **Deployment** | Azure App Service (Sweden Central) |
| **AI-Assisted Dev** | GitHub Copilot |

---

## 🚀 Local Setup

### Prerequisites

- Python 3.10+
- Azure OpenAI deployment (Microsoft Foundry IQ)

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/hackermind.git
cd hackermind

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Create a .env file with:
# AZURE_OPENAI_KEY=your-key
# AZURE_OPENAI_ENDPOINT=your-endpoint
# AZURE_OPENAI_DEPLOYMENT=hackermind-gpt

# Start the server
python app.py
```

Open your browser at `http://127.0.0.1:5000`

### Environment Variables

```env
AZURE_OPENAI_KEY=your-azure-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=hackermind-gpt
```

---

## 🔌 API Reference

### `POST /api/analyze`

Triggers the full five-agent pipeline for a given system description.

**Request:**
```json
{
  "system_description": "A web application with login page, MySQL database, REST API hosted on AWS EC2 with admin panel accessible from internet"
}
```

**Response:**
```json
{
  "analysis": "System architecture analysis...",
  "vulnerabilities": "Identified attack vectors...",
  "defenses": "Defense strategies...",
  "report": "Full security report...",
  "scores": {
    "sql_injection": 75,
    "xss": 60,
    "auth_bypass": 80,
    "api_security": 65,
    "data_exposure": 85,
    "network_attack": 70
  },
  "overall_risk": 72
}
```

---

## 🤖 GitHub Copilot Usage

GitHub Copilot was used throughout the entire development of HackerMind:

**Architecture & Design (Copilot Chat)**
- Designed the sequential multi-agent pipeline architecture — ensuring each agent's output feeds the next as context
- Reasoned through the Flask route structure and JSON response schema
- Debugged Azure OpenAI API integration — correct endpoint format, api-key header vs Authorization header
- Explored error handling patterns for agent failures and API timeouts

**Code Acceleration (Copilot Suggestions)**
- Auto-completed all five agent functions with correct system prompt engineering
- Generated the `call_azure` abstraction layer used across all agents
- Completed the risk score parsing with JSON extraction and fallback defaults
- Suggested the sequential agent chaining pattern in `app.py`

**Frontend Development**
- Generated the 3D perspective map CSS transforms and mouse-reactive JavaScript
- Completed the terminal-style progress animation with step-based labeling
- Built the live analyst feed with random insight generation and DOM management
- Designed the hologram card CSS with scanline animations and glow effects

---

## 🏆 Judging Criteria Alignment

| Criteria | Weight | How HackerMind Delivers |
|----------|--------|------------------------|
| **Accuracy & Relevance** | 20% | Fully meets Creative Apps requirements. Microsoft Foundry IQ is the core intelligence engine powering all five agents. GitHub Copilot used and documented throughout. Deployed live on Azure. |
| **Reasoning & Multi-step Thinking** | 20% | True sequential multi-agent reasoning chain — each agent builds on prior output. AGENT_ANALYZER → AGENT_ATTACKER → AGENT_DEFENDER → AGENT_REPORTER → AGENT_SCORER is a genuine reasoning pipeline, not parallel calls. |
| **Creativity & Originality** | 15% | A cyberpunk-themed multi-agent security intelligence platform. The 3D interactive risk map, live analyst feed, and immersive terminal UI create an experience unlike any standard security tool. |
| **User Experience & Presentation** | 15% | Fully deployed on Azure App Service. Judges can analyze any system immediately. Hologram panels, animated scanlines, glitch effects, and a live 3D threat map make the experience genuinely memorable. |
| **Reliability & Safety** | 20% | No credentials in repository. All secrets managed via Azure App Service environment variables. Graceful fallback scoring if agent fails. No PII stored. Production deployment on Azure. |
| **Community Vote** | 10% | "Describe any system and five AI agents will instantly analyze it, find vulnerabilities, and build defenses" is an immediately shareable concept. The live demo is compelling in under 30 seconds. |

---

## 🔒 Security

✅ No API keys or credentials committed to this repository  
✅ All secrets managed via Azure App Service environment variables  
✅ `.env` is gitignored  
✅ No customer PII stored  
✅ No confidential or proprietary information in this repository  

---

## 👩‍💻 About the Creator

Hi, I'm **Rhea Prajapati** — a cybersecurity and digital forensics student who builds at the intersection of security, AI, and modern web technologies.

HackerMind was born from a simple question: *what if you could describe any system and five specialized AI agents would instantly analyze its architecture, identify every vulnerability, suggest defense strategies, generate a full security report, and calculate your risk score — all in one pipeline?*

My areas of interest:
- 🔐 Cybersecurity & Digital Forensics
- ☁️ Cloud Security  
- 🌐 Web Application Security
- 🔌 API Security
- 🤖 AI in Security
- ⚔️ Ethical Hacking

Always learning. Always building. Always securing.

---

## 👤 Author

**Rhea Prajapati**  
GitHub: [@rh3eeacysec](https://github.com/rh3eeacysec)
Microsoft Learn: Rhea-8387

*Built for Microsoft Agents League Hackathon 2026 — Creative Apps Track*  
*Powered by Microsoft Foundry IQ*

---

**Five agents. One target. The truth about your system's security — in seconds.**
```

