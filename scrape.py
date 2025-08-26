from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import time
import os
import sys

DEBUG = True  # Toggle this to False when you're done inspecting HTML

def get_followers(username):
    url = f"https://www.tiktok.com/@{username}"
    print(f"Loading TikTok profile: {url}")

    # Set up ChromeDriver
    service = Service("C:/Users/kento/Documents/GitHub/chromedriver-win64/chromedriver.exe")  # Adjust path if needed
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    print(f"Final URL after redirects: {driver.current_url}")

    # Wait for follower count element to appear
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "strong[data-e2e='followers-count']"))
        )
        print("Follower count element detected.")
    except:
        print("Timeout waiting for follower count element.")

    # Save HTML for inspection
    html = driver.page_source
    if DEBUG:
        html_path = os.path.abspath("page.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Saved HTML to: {html_path}")

    driver.quit()

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    # Extract follower count using data-e2e attribute
    try:
        tag = soup.find("strong", {"data-e2e": "followers-count"})
        count = tag.text.strip()
        print(f"Extracted follower count: {count}")
    except Exception as e:
        print(f"Failed to extract follower count: {e}")
        count = "N/A"

    return count

def save_json(count):
    data = {
        "frames": [
            {
                "text": f"Followers: {count}",
                "icon": None
            }
        ]
    }
    with open("followers.json", "w") as f:
        json.dump(data, f)
    print("Saved follower count to followers.json")

if __name__ == "__main__":
    username = sys.argv[1] if len(sys.argv) > 1 else "theduckstore1920"
    count = get_followers(username)
    save_json(count)