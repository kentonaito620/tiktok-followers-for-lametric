from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import time

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
    print("Page loaded, waiting for content...")
    time.sleep(5)  # Let the page fully render

    # Save HTML for inspection
    html = driver.page_source
    with open("page.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Saved HTML to page.html")

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")
    driver.quit()

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
    username = "theduckstore1920"
    count = get_followers(username)
    save_json(count)
