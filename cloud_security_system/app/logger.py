import json
import os
from datetime import datetime

LOG_FILE = "data/logs.json"

def save_log(log_data):
    try:
        # Ensure data folder exists
        if not os.path.exists("data"):
            os.mkdir("data")

        # Add timestamp if missing
        if not log_data.get("timestamp"):
            log_data["timestamp"] = str(datetime.utcnow())

        logs = []

        # Load existing logs
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                try:
                    logs = json.load(f)
                except Exception:
                    logs = []

        # Append new log
        logs.append(log_data)

        # Save logs
        with open(LOG_FILE, "w") as f:
            json.dump(logs, f, indent=4)

        return log_data

    except Exception as e:
        print("ERROR OCCURRED:", e)
        return {"error": str(e)}