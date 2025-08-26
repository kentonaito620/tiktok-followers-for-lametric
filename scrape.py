import requests
from bs4 import BeautifulSoup
import json

def get_followers(username):
    url = f"https://www.tiktok.com/@theduckstore1920"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        text = soup.find("meta", {"name": "description"})["content"]
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
