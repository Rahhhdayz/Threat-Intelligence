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
├──app.py # Streamlit App (optional)
├── main.py # Core script
├── otx_collector.py # Downloads and parses OTX feed
├── feed_parser.py # Parses RSS feed and saves to JSON
├── extractors/
│ ├── regex_extractor.py # Regex-based IOC extraction
│ └── nlp_extractor.py # Named Entity Recognition using spaCy
├── enrichment/
│ ├── virus_total.py # VirusTotal enrichment for hashes
│ └── ip_enrich.py # AbusedIPDB enrichment for IPs
├── otx_iocs.json # Raw OTX feed (output)
├── rss_iocs.json # Raw RSS feed (output)
├── merged_iocs.json # Final normalized IOCs
└── requirements.txt # Python dependencies

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Rahhhdayz/Threat-Intelligence
cd Threat-Intelligence

### 2. Install Python dependencies:
pip install -r requirements.txt

### 3. Set your API keys in a .env file:
VT_API_KEY=your_virustotal_key
SHODAN_API_KEY=your_shodan_key

### 4. Run the aggregator
python main.py
