from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import time

def get_followers(username):
    url = f"https://www.tiktok.com/@{username}"
    service = Service("C:/Users/kento/Documents/GitHub/chromedriver-win64/chromedriver.exe")  # Update path if needed

    options = Options()
    options.add_argument("--headless")  # Run without opening a browser window
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")  # Suppress warnings

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(5)  # Let the page load fully

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    try:
        meta = soup.find("meta", {"name": "description"})
        text = meta["content"]
        count = text.split("Followers")[0].split()[-1]
    except Exception:
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

if __name__ == "__main__":
    username = "theduckstore1920"
    count = get_followers(username)
    save_json(count)
