# Net-Watch: Tactical Port Scanner 🛡️

A multi-threaded network reconnaissance tool designed for rapid port scanning and service banner grabbing. Built to demonstrate raw socket programming and concurrency in Python.

## 🚀 Features
* **Multi-Threaded Architecture:** Utilizes 100+ concurrent threads for high-speed scanning.
* **Banner Grabbing:** Attempts to retrieve service version information (SSH, HTTP, FTP headers) from open ports.
* **Stealth/Speed:** Customizable timeout settings.
* **Clean UI:** Color-coded terminal output using `colorama`.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Networking:** `socket` (Raw TCP/IP connections)
* **Concurrency:** `threading`, `queue` (Thread pool management)

## ⚠️ Disclaimer
**Authorized Use Only:** This tool is intended for educational purposes and security testing on networks you own or have explicit permission to audit. Unauthorized scanning of third-party networks is illegal.

## ⚡ Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
