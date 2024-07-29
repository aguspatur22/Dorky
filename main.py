from fetcher import fetch_ghdb_xml
from parser import parse_ghdb_xml
from checker import check_dork
from notifier import send_email
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    xml_content = fetch_ghdb_xml()
    entries = parse_ghdb_xml(xml_content)
    domain = os.getenv('DOMAIN')

    for dork in entries:
        url = check_dork(dork)
        if url:
            print(f"Dork Found! The following dork was found: {url}")
            #Send mail
    urls = map(lambda x: f"https://www.google.com/search?q={x} site:*.{domain}", entries)
    print("Dorks checked: ", *urls, sep='\nURL: ')

if __name__ == "__main__":
    main()