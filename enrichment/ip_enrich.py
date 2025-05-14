import requests
import os

def enrich_ip_abuseipdb(ip):
    api_key = os.getenv("ABUSEIPDB_API_KEY")
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": api_key,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90  # check abuse reports from last 90 days
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()["data"]
        return {
            "ip": ip,
            "abuseConfidenceScore": data["abuseConfidenceScore"],
            "totalReports": data["totalReports"],
            "countryCode": data.get("countryCode", "N/A"),
            "domain": data.get("domain", "N/A"),
            "isPublic": data.get("isPublic", False)
        }
    except Exception as e:
        print(f"[!] Error enriching IP {ip}: {e}")
        return {"ip": ip, "error": str(e)}
