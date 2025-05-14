# Threat Feed Aggregator with IOC Extraction & Enrichment

This project is a custom-built **Threat Feed Aggregator** designed for Cyber Threat Intelligence (CTI) purposes. It ingests threat data from various open-source feeds, extracts relevant **Indicators of Compromise (IOCs)**, enriches them using external threat intelligence APIs, and prepares a normalized JSON output for analysis or visualization.

##  Features

- IOC extraction using **regex** and **NLP (spaCy)**:
  - IP addresses, domains, URLs, hashes, CVEs
  - Named entities (ORG, PERSON, PRODUCT, etc.)
- Data aggregation from:
  - AlienVault OTX JSON Feeds
  - Cybersecurity-related RSS feeds
- OC enrichment via:
  - **VirusTotal** (for hashes)
  - **AbusedIPDB** (for IPs)
- [Optional] Streamlit dashboard for interactive IOC visualization

## Folder Structure
<img width="608" alt="image" src="https://github.com/user-attachments/assets/b0693334-e854-475c-984f-8f8872852bbb" />


## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Rahhhdayz/Threat-Intelligence
cd Threat-Intelligence
```

### 2. Install Python dependencies:
```bash
pip install -r requirements.txt
```
### 3. Set your API keys in a .env file:
```bash
VT_API_KEY=your_virustotal_key
SHODAN_API_KEY=your_shodan_key
```

### 4. Run the aggregator
```bash
python main.py
```
