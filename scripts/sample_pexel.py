import requests
from io import BytesIO
CHUNK_SIZE = 2048
url = "https://api.pexels.com/videos/search?query=nature&per_page=1&orientation=portrait&size=medium"





r = requests.get(url, headers={'Authorization': 'p1p0I9iC7ChShttx4Z29WDLsyfW6V6mSm05l0cE0evnxyYckEdCFqkEl'})


ri = requests.get("https://api.pexels.com/videos/videos/{}".format(r.json()["videos"][0]["id"]), headers={'Authorization': 'p1p0I9iC7ChShttx4Z29WDLsyfW6V6mSm05l0cE0evnxyYckEdCFqkEl'})
for i in ri.json()["video_files"]:
    if i["quality"] == "hd" and i["width"] == 1080:
        ro = requests.get(i["link"], headers={'Authorization': 'p1p0I9iC7ChShttx4Z29WDLsyfW6V6mSm05l0cE0evnxyYckEdCFqkEl'})
        # print(r.text)
     
        with open("data/input.mp4",'wb') as f:
          f.write(ro.content)



 #  curl -H "Authorization: p1p0I9iC7ChShttx4Z29WDLsyfW6V6mSm05l0cE0evnxyYckEdCFqkEl" "https://api.pexels.com/videos/search?query=nature&per_page=1"