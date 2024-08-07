import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def check_dork(dork):
    domain = os.getenv('DOMAIN')
    query = f"{dork} site:*.{domain}"
    url = f"https://www.google.com/search?q={query}"

    agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

    options = uc.ChromeOptions()
    options.add_argument(f"user-agent={agent}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = uc.Chrome(options=options)

    driver.get(url)
    
    print("[*] Fetching ", url, " please wait...")
    
    time.sleep(10)  # Adjust sleep time as needed for page load and search results to appear
    try:
        # Find all search result elements
        search_results = driver.find_elements(By.CLASS_NAME, 'g')

        body = driver.find_element(By.TAG_NAME, 'body')
        for _ in range(3):
            ActionChains(driver).send_keys(Keys.END).perform()
            time.sleep(2)

        for result in search_results:
            if domain in result.text:
                driver.quit()
                return url

    except Exception as e:
        print(f"Error occurred: {str(e)}")

    driver.quit()
    return ""