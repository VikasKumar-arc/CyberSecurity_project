# Network Intrusion Detection and Real-Time Security Monitoring System

## Project Overview
Cyber Security Network Monitor is a Python-based cybersecurity application that captures network traffic, analyzes packets, detects suspicious activities, stores security events, and displays monitoring information through a dashboard.

## Features
- Live packet monitoring using Scapy
- Packet logging with timestamp, IP, protocol and size
- Rule-based intrusion detection
- Port scan detection
- Suspicious traffic detection
- SQLite event storage
- Flask dashboard
- Traffic statistics visualization

## Installation

```bash
git clone <repository-url>
cd CyberSecurity_Network_Monitor
pip install -r requirements.txt
```

## Run Project

Start monitoring:

```bash
python src/main.py
```

Start dashboard:

```bash
python dashboard/app.py
```

Open:
http://127.0.0.1:5000

## Screenshots

Add screenshots inside the screenshots folder:
- dashboard.png
- traffic_monitor.png
- alert_detection.png

## Technologies Used
- Python 3
- Scapy
- SQLite
- Flask
- Pandas
- Matplotlib

## Project Structure
See repository folders for modular implementation.

## GitHub Usage
Commit all files and push:

```bash
git add .
git commit -m "Initial cybersecurity monitoring project"
git push origin main
```

## Author
Cybersecurity Project