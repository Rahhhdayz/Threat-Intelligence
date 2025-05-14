# enrichment/virustotal.py
import requests
import time

def enrich_hashes_vt(api_key, hashes, delay=15):
    
    enriched = {}
    headers = {"x-apikey": api_key}

    for h in hashes:
        url = f"https://www.virustotal.com/api/v3/files/{h}"
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            json_data = res.json()
            enriched[h] = {
                "malicious": json_data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("malicious", 0),
                "suspicious": json_data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("suspicious", 0),
                "harmless": json_data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("harmless", 0)
            }
        else:
            enriched[h] = None
        time.sleep(delay)  # Respect VT free API rate limit

    return enriched
