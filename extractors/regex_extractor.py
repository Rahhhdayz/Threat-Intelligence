import re

def extract_iocs(text):
    return {
        "ips": re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", text),
        "domains": re.findall(r"\b(?:[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?\.)+[a-z]{2,}\b", text, re.IGNORECASE),
        "urls": re.findall(r"https?://[^\s]+", text),
        "hashes": re.findall(r"\b(?:[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b", text),
        "cves": re.findall(r"CVE-\d{4}-\d{4,7}", text)
    }