# LogSentinel – Security Log Analysis & Event Detection Tool (Prototype)

LogSentinel is a **work-in-progress security log analysis project** built in Python.  
The goal is to simulate the early stages of a SIEM workflow:

**Log ingestion → Parsing → Detection → Reporting**

This project is part of my final year work, and I am actively expanding it with new parsing
methods and security detection rules.


## Current Prototype Features

The current working version includes:

### Log Ingestion
Reads data from a sample authentication log file (`sample_auth.log`)

### Regex-Based Parsing
Extracts:
- timestamp  
- log level  
- login action (successful / failed)  
- username  
- source IP address  

### Failed Login Detection
Counts failed login attempts per IP  
Flags IPs with **5 or more failed attempts** → brute-force indicator

### Clean Console Report
Generates an easy-to-read summary showing:
- total log lines  
- successfully parsed entries  
- failed login counts  
- suspicious IP addresses  

---

## 📂 Project Structure

