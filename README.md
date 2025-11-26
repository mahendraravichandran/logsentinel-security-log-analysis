# LogSentinel – Security Log Analysis & Event Detection Tool (Prototype)

LogSentinel is a **Python-based security log analysis project** designed to simulate the core stages of a SIEM workflow:

**Log ingestion → Parsing → Detection → Reporting**

This is an active **final-year work-in-progress project**, focused on building a lightweight detection engine capable of identifying suspicious authentication behavior using simple rule-based analysis.

---

## 🚀 Current Prototype Features

The current prototype includes the essential components needed to parse authentication logs and detect abnormal login activity.

---

### 🔹 Log Ingestion  
Reads log data from a sample authentication log file (`sample_auth.log`).

---

### 🔹 Regex-Based Parsing  
Each log entry is processed using Python regular expressions to extract key fields:

- Date and time  
- Log level (INFO / WARN)  
- Login action (successful / failed)  
- Username  
- Source IP address  

---

### 🔹 Failed Login Detection  
Implements a basic brute-force detection rule:

- Counts failed login attempts per IP address  
- Flags IPs with **5 or more failed attempts**  
- Helps identify repeated login failures from the same source (possible brute-force)

---

### 🔹 Clean Console Report  
After analysis, the tool generates a readable summary showing:

- Total number of log entries  
- Number of successfully parsed entries  
- Failed login counts per IP  
- Suspicious IPs exceeding the detection threshold  

Example output:

