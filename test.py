import requests
import json

class MyRedfinScraper:
    def __init__(self):
        self.session = requests.Session()
        # Update session to mimic a browser
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/117.0.0.1 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;"
                "q=0.9,image/webp,*/*;q=0.8"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.redfin.com/",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Sec-CH-UA": '"Chromium";v="117", "Not;A=Brand";v="24"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"Windows"',
        })

        # Start a real session by visiting the homepage to set cookies
        self.session.get("https://www.redfin.com")

    def location_autocomplete(self, query):
        url = "https://redfin.com/stingray/do/location-autocomplete"
        params = {"location": query, "v": 2}
        resp = self.session.get(url, params=params)
        resp.raise_for_status()

        # Redfin’s JSON typically starts with `{}&&`
        raw_text = resp.text
        idx = raw_text.find('{')
        if idx > 0:
            raw_text = raw_text[idx:]
        return json.loads(raw_text)

# Usage
client = MyRedfinScraper()
try:
    response = client.location_autocomplete("126 CUYAHOGA CT,PERRIS,CA 92570")
    print(json.dumps(response, indent=2))
except requests.HTTPError as e:
    print("Got 403 again:", e)
