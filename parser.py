import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def parse_ghdb_xml(xml_content):
    root = ET.fromstring(xml_content)
    entries = []

    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    print("Date of dorks: ", yesterday)
    for entry in root.findall('entry'):
        date = entry.find('date').text
        if date == yesterday:
            query = entry.find('query').text
            entries.append(query)
    return entries
