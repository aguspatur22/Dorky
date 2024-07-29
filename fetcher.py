import requests

def fetch_ghdb_xml():
    print("[*] Fetching Google Hacking Database...")
    url = "https://gitlab.com/exploit-database/exploitdb/-/raw/main/ghdb.xml"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.content