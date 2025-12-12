import random
from datetime import datetime, timedelta

def get_dashboard_stats():
    """Generate mock dashboard statistics"""
    return {
        "total_scans": random.randint(1000, 5000),
        "scans_today": random.randint(50, 200),
        "vulnerabilities_found": random.randint(100, 500),
        "critical_issues": random.randint(5, 25)
    }

def get_chart_data():
    """Generate mock chart data for the last 7 days"""
    labels = []
    data = []
    
    for i in range(7, 0, -1):
        date = datetime.now() - timedelta(days=i)
        labels.append(date.strftime("%b %d"))
        data.append(random.randint(20, 100))
    
    return {
        "labels": labels,
        "data": data
    }

def get_recent_scans():
    """Generate mock recent scan data"""
    scan_types = ["Security Audit", "Code Quality", "Dependency Check", "Performance Analysis"]
    statuses = ["Completed", "In Progress", "Failed"]
    
    scans = []
    for i in range(5):
        scans.append({
            "id": f"SCAN-{random.randint(1000, 9999)}",
            "type": random.choice(scan_types),
            "status": random.choice(statuses),
            "timestamp": (datetime.now() - timedelta(hours=random.randint(1, 48))).strftime("%Y-%m-%d %H:%M")
        })
    
    return scans
