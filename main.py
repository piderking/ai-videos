import os, requests
from bs4 import BeautifulSoup
import json
import re
import requests

# Fore testing $ENV:URLS="https://www.reddit.com/r/AmItheAsshole/comments/1bzq7j5/aita_for_naming_my_son_after_my_father_instead_of/"
links = os.environ.get("URLS").split(";")

print(links)

# JSON Data from Reddit
#table = requests.get("https://www.reddit.com/r/AmItheAsshole/hot.json",).json()
table = json.loads(open("hot.json", "r").read())


# Where all the titles/text will be generated to
titles = []
texts = []

# HTTP Headers for 11 Labs
headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "c798607f1c366ac93066a74e50a10d4f"
}
CHUNK_SIZE = 2048

# Start of Scripting---------
for tabe in table["data"]["children"]:
    if tabe["data"]["url"] in links: # Only do articles where the URL is provided
        titles.append(tabe["data"]["title"])
        texts.append(tabe["data"]["selftext"])
        
        


for text in texts:
    data = {
    "text": text,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
    }

    if not os.path.exists("data/tts.mp3"):
        print("Downloading New Recording")
        response = requests.post("https://api.elevenlabs.io/v1/text-to-speech/j9jfwdrw7BRfcR43Qohk", json=data, headers=headers)
        with open('data/tts.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
    print("Voice Recordings Finished")