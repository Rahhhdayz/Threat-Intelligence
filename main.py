import json
import os
from extractors.regex_extractor import extract_iocs
from extractors.nlp_extractor import extract_entities
from enrichment.virus_total import enrich_hashes_vt 
from enrichment.ip_enrich import enrich_ip_abuseipdb 

# Load API keys
VT_API_KEY = os.getenv("VT_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

# Load OTX JSON
with open('otx_iocs.json') as f:
    otx_raw = json.load(f)
    otx_text = json.dumps(otx_raw)

# Load RSS JSON
with open('rss_iocs.json') as f:
    rss_raw = json.load(f)
    rss_text = json.dumps(rss_raw)

# Extract IOCs
otx_iocs = extract_iocs(otx_text)
rss_iocs = extract_iocs(rss_text)

# Combine the IOCs
merged_iocs = {
    "ips": list(set(otx_iocs["ips"] + rss_iocs["ips"])),
    "domains": list(set(otx_iocs["domains"] + rss_iocs["domains"])),
    "urls": list(set(otx_iocs["urls"] + rss_iocs["urls"])),
    "hashes": list(set(otx_iocs["hashes"] + rss_iocs["hashes"])),
    "cves": list(set(otx_iocs["cves"] + rss_iocs["cves"]))
}

# Extract NLP entities from full article text
combined_text = ""
for item in otx_raw + rss_raw:
    combined_text += " " + item.get("title", "")
    combined_text += " " + item.get("summary", "")
    combined_text += " " + item.get("description", "")
entities = extract_entities(combined_text)
merged_iocs["named_entities"] = entities

# Enrich IPs using AbuseIPDB
ips = merged_iocs.get("ips", [])
enriched_ips = []
for ip in ips:
    enriched_data = enrich_ip_abuseipdb(ip)
    enriched_ips.append(enriched_data)

merged_iocs["enriched_ips"] = enriched_ips

# Save to file
with open('final_merged_iocs.json', 'w') as f:
    json.dump(merged_iocs, f, indent=4)
