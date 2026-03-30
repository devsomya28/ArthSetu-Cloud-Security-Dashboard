🔐 Cloud Security & Threat Detection System

A simple cloud security monitoring system that detects suspicious activities, alerts administrators, and logs security events using rule-based and AI-based techniques.

📌 Problem Statement

Develop a system that:

Detects suspicious activities
Sends alerts to admin
Maintains logs of security events
🛠️ Tech Stack
Frontend/UI: Streamlit
Backend: Python
Data Handling: Pandas
AI/ML: Scikit-learn (Isolation Forest)
⚙️ System Architecture
What is this?
🔁 Workflow
System generates or receives activity logs
Logs are analyzed using:
Rule-based detection
AI anomaly detection
If suspicious activity is detected:
Alert is shown on dashboard
Event is logged
All logs are displayed and stored for monitoring
📂 Project Structure
.
├── app.py              # Main application (UI + detection logic)
├── requirements.txt   # Dependencies
└── README.md          # Documentation
🧠 Threat Detection Logic
Rule-Based Detection
def rule_detection(log):
    if log["failed_logins"] > 5:
        return "Brute Force Attack"
    elif log["data_transfer"] > 800:
        return "Data Exfiltration"
    return "Normal"
🤖 AI-Based Detection
Uses Isolation Forest
Detects unusual patterns in:
Login attempts
Data transfer
🚨 Alert System
Alerts displayed in dashboard
Highlights suspicious logs
Shows total threats detected
📝 Logging System
All logs stored in memory (session)
Displayed in real-time table
Can be extended to file/database
📊 Features
🔍 Detects suspicious activities
🚨 Real-time alerts
📝 Log monitoring system
🤖 AI-based anomaly detection
📊 Interactive dashboard
⚡ How to Run
1️⃣ Install dependencies
pip install streamlit pandas scikit-learn
2️⃣ Run application
python -m streamlit run app.py
3️⃣ Open in browser
https://arthsetu-cloud-security-dashboard-12.onrender.com/
🧪 Usage
Click "Generate New Logs"
View logs in dashboard
Check Alerts section for threats
Analyze anomalies detected by AI
🔔 Example Threats
🚨 Brute Force Attack (high failed logins)
🚨 Data Exfiltration (high data transfer)
🚨 Unknown anomalies (AI detected)
📌 Future Improvements
📧 Email alerts to admin
🔐 Login authentication system
☁️ Cloud deployment
📊 Advanced analytics dashboard
👨‍💻 Author
somya devda
https://github.com/devsomya28
⭐ Conclusion
This project demonstrates a basic cloud security system that monitors logs, detects threats using rule-based and AI techniques, alerts administrators, and maintains logs for analysis.
