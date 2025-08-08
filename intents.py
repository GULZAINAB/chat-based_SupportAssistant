def classify_intent(query: str) -> str:
    query = query.lower()
    if "wifi" in query or "internet" in query:
        return "Network Issue"
    elif "restart" in query:
        return "System Restart"
    elif "date" in query or "time" in query:
        return "System Settings"
    elif "cache" in query or "driver" in query:
        return "General Maintenance"
    else:
        return "General Support"
