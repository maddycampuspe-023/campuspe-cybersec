# Network Scanning Automation

## Project Description
This project automates basic network scanning tools using Python. It includes three main tools:

- Ping Scanner
- ARP Scanner
- Nmap Scanner

These tools help perform network reconnaissance tasks such as checking host availability, retrieving ARP table entries, and scanning network ports.

---

## Requirements

- Python 3.x
- Nmap installed
- Linux (Kali) 

---

## Installation

### Install Python
Check version:
```bash
python3 --version

How to Run
1. Ping Scanner
python3 ping_scanner.py

Features:

Single host scan
Multiple host scan
Shows average response time


2. ARP Scanner
python3 arp_scanner.py

Features:

Retrieves ARP table
Displays IP-MAC mapping
Saves results to file


3. Nmap Scanner
python3 nmap_scanner.py

Features:

Host discovery
Port scanning
Service detection
OS detection
Save results to file