from fetcher import fetch_ghdb_xml
from parser import parse_ghdb_xml
from checker import check_dork
from notifier import MailLog
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    xml_content = fetch_ghdb_xml()
    entries = parse_ghdb_xml(xml_content)
    domain = os.getenv('DOMAIN', "No domain set")
    print(f"DOMAIN: {domain}")

    dork_urls = []
    for dork in entries:
        url = check_dork(dork)
        if url:
            print(f"Dork Found! The following dork was found: {url}")
            dork_urls.append(url)
    
    if dork_urls:
        mail_log = MailLog(
            name='Dorky',
            me=os.getenv('EMAIL_USER'),
            recipients=[os.getenv('RECIPIENT_EMAIL')],
            mail_server=os.getenv('SMTP_SERVER'),
            smtp_port=os.getenv('SMTP_PORT'),
            email_user=os.getenv('EMAIL_USER'),
            email_password=os.getenv('EMAIL_PASSWORD')
        )
        mail_log.send_report(dork_urls)
        print("Email sent!")

    urls = map(lambda x: f"https://www.google.com/search?q={x} site:*.{domain}", entries)
    print("Dorks checked: ", *urls, sep='\nURL: ')

if __name__ == "__main__":
    main()