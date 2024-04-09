import os, requests
from bs4 import BeautifulSoup
import json
# Fore testing $ENV:URLS="https://www.reddit.com/r/AmItheAsshole/comments/1bzneq5/aita_for_selling_the_gift_my_exgirlfriend_bought/;https://www.reddit.com/r/AmItheAsshole/comments/1bzneq5/aita_for_selling_the_gift_my_exgirlfriend_bought/"
links = os.environ.get("URLS").split(";")


#table = requests.get("https://www.reddit.com/r/AmItheAsshole/hot.json",).json()

table = json.loads(open("hot.json", "r").read())


for tabe in table["data"]["children"]:
    print("----------------------------------------------------------")
    if tabe["data"]["url"] in links:
        print(tabe["data"]["url"])
    #print(table["data"]["children"][2]["data"]["selftext"])


for link in links:
    print(link.split("/")[7])
