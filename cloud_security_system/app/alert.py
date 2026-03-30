def send_alert(threat):
    if threat:
        print("\n🚨 SECURITY ALERT 🚨")
        print("Threat Type:", threat.get("threat"))
        print("Message:", threat.get("message"))
        print("--------------------------\n")