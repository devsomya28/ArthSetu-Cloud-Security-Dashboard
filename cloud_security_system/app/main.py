from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from .logger import save_log
from app.detector import detect_threat
from app.alert import send_alert

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for UI history
logs_db = []

# Define log structure
class Log(BaseModel):
    user_id: str
    ip_address: str
    action: str
    timestamp: str = None

@app.get("/")
def home():
    return {"message": "Cloud Security System Running"}

# POST API to receive logs
@app.post("/logs")
def receive_log(log: Log):
    log_dict = log.dict()

    saved_log = save_log(log_dict)

    threat = detect_threat(log_dict)

    send_alert(threat)

    # ✅ Store for history
    logs_db.append({
        "user_id": log.user_id,
        "ip_address": log.ip_address,
        "action": log.action,
        "threat": threat
    })

    return {
        "message": "Log stored successfully",
        "data": saved_log,
        "threat": threat
    }

# ✅ NEW: GET API for UI history
@app.get("/logs")
def get_logs():
    return logs_db