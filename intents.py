# intents.py
def classify_intent(query: str) -> str:
    q = query.lower()
    if any(k in q for k in ["wifi", "wi-fi", "internet", "no connection", "router", "ssid"]):
        return "Network Issue"
    if any(k in q for k in ["restart", "reboot", "shut down", "power off"]):
        return "System Restart"
    if any(k in q for k in ["date", "time", "timezone", "clock"]):
        return "System Settings"
    if any(k in q for k in ["cache", "clear cache", "cookie", "browser cache"]):
        return "Browser / Cache"
    if any(k in q for k in ["driver", "update driver", "install driver"]):
        return "Drivers / Updates"
    return "General Support"
