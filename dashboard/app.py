import streamlit as st
import json

# Load Merged IOCs
def load_ioc_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return {}

# UI Setup
st.set_page_config(page_title="Threat Feed Dashboard", layout="wide")
st.title("Threat Feed Dashboard")

# Load the merged feed
ioc_data = load_ioc_json("../final_merged_iocs.json")

# Select IOC type from sidebar
ioc_type = st.sidebar.selectbox("Choose IOC Type", ["ips", "domains", "urls", "hashes", "cves"])
selected_iocs = ioc_data.get(ioc_type, [])

# Display IOC Info
st.subheader(f"{ioc_type.upper()} ")
st.metric(label="Total IOCs", value=len(selected_iocs))
st.dataframe(selected_iocs, use_container_width=True)

# Optional: Download
st.download_button(
    label="Download IOC JSON",
    data=json.dumps({ioc_type: selected_iocs}, indent=2),
    file_name=f"merged_{ioc_type}.json",
    mime="application/json"
)
