"""
You are given a stream of alerts from multiple services. Each alert has a service_id, timestamp, and message. 
Write a function that deduplicates alerts within a 5-minute window for the same service and message.
(Follow up can be, make the window configurable, handle different time stamps for different Services).

"""

from datetime import timedelta, datetime

def deduplicate_alerts(alerts, window_minutes=5):
    # Convert window size to a timedelta (e.g., 5 minutes)
    window = timedelta(minutes=window_minutes)
    
    # Dictionary to store the last timestamp for each (service_id, message) pair
    last_seen = {}
    
    # List to store deduplicated alerts
    deduped = []
    
    # Process each alert
    for alert in alerts:
        # Get the timestamp as a datetime object
        ts = datetime.fromisoformat(alert['timestamp'])
        
        # Create a unique key for this service and message
        key = (alert['service_id'], alert['message'])
        
        # Check if this is a new alert or outside the time window
        if key not in last_seen or (ts - last_seen[key]) > window:
            # Keep this alert
            deduped.append(alert)
            # Update the last seen timestamp for this key
            last_seen[key] = ts
    
    return deduped


# Test with sample alerts
alerts = [
    {"service_id": "svc1", "timestamp": "2025-09-06T10:00:00", "message": "Error X"},
    {"service_id": "svc1", "timestamp": "2025-09-06T10:03:00", "message": "Error X"},
    {"service_id": "svc1", "timestamp": "2025-09-06T10:07:00", "message": "Error X"},
    {"service_id": "svc2", "timestamp": "2025-09-06T10:01:00", "message": "Error Y"},
]

result = deduplicate_alerts(alerts)
for alert in result:
    print(f"{alert['service_id']}, {alert['timestamp']}, \"{alert['message']}\"")