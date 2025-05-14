import requests
import json
from datetime import datetime

def fetch_otx_iocs(api_key, section="general", indicator_type="IPv4", modified_since=None):
    url = f"https://otx.alienvault.com/api/v1/indicators/export?type={indicator_type}&section={section}"
    if modified_since:
        url += f"&modified_since={modified_since}"
    
    headers = {"X-OTX-API-KEY": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")

def parse_iocs(raw_text):
    return [line.strip() for line in raw_text.splitlines() if line.strip()]

def save_iocs_to_json(iocs, filename):
    data = [{"ioc": ioc, "source": "otx", "type": "unknown"} for ioc in iocs]
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[+] Saved {len(iocs)} OTX IOCs to {filename}")

if __name__ == "__main__":
    api_key = "[Your_API_KEY]"
    indicator_type = "IPv4"
    modified_since = "2024-01-01T00:00:00"
    output_file = f"otx_iocs.json"

    try:
        raw_data = fetch_otx_iocs(api_key, indicator_type=indicator_type, modified_since=modified_since)
        ioc_list = parse_iocs(raw_data)
        save_iocs_to_json(ioc_list, output_file)
    except Exception as e:
        print(f"[!] Error: {e}")

