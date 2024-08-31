import requests
import json
from datetime import datetime

WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"

def fetch_most_edited_pages():
    params = {
        "action": "query",
        "list": "recentchanges",
        "rctype": "edit",
        "rcprop": "title|timestamp",
        "rclimit": 500,
        "format": "json"
    }
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    return response.json()

def save_data_to_json(data):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"data/{today}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    data = fetch_most_edited_pages()
    save_data_to_json(data)
