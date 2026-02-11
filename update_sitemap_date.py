#!/usr/bin/env python3
import xml.etree.ElementTree as ET
from datetime import datetime

# Parse the sitemap XML
tree = ET.parse("sitemap.xml")
root = tree.getroot()

# Define namespace
ns = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}

# Get today's date in YYYY-MM-DD format
today = datetime.now().strftime("%Y-%m-%d")

# Update all <lastmod> tags
for url in root.findall(".//ns:url", ns):
    lastmod = url.find("ns:lastmod", ns)
    if lastmod is not None:
        lastmod.text = today

# Write back to file
tree.write("sitemap.xml", encoding="UTF-8", xml_declaration=True)
print(f"Sitemap updated with date: {today}")
