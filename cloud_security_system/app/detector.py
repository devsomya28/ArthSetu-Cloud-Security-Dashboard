from datetime import datetime, timedelta

# Store attempts per IP
attempt_store = {}

def detect_threat(log):
    ip = log["ip_address"]
    action = log["action"]
    now = datetime.now()

    # Initialize IP entry
    if ip not in attempt_store:
        attempt_store[ip] = []

    # Add current attempt
    attempt_store[ip].append(now)

    # Keep only last 5 minutes
    attempt_store[ip] = [
        t for t in attempt_store[ip]
        if now - t < timedelta(minutes=5)
    ]

    count = len(attempt_store[ip])

    # Detection rule
    if action == "login_failed" and count >= 5:
        return {
            "threat": "Brute Force Attack",
            "message": f"{count} failed attempts from IP {ip}",
            "attempt_count": count
        }

    return {
        "threat": None,
        "attempt_count": count
    }