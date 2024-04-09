import requests

CHUNK_SIZE = 2048
url = "https://api.elevenlabs.io/v1/text-to-speech/j9jfwdrw7BRfcR43Qohk"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "c798607f1c366ac93066a74e50a10d4f"
}

data = {
  "text": """
    AITA for refusing to go into Hooters for my brother’s 18th birthday and sitting in the car?
I’m 14f and just last week my older brother turned 18. He is at college a few hours away so my mom, dad and I got in the car to meet him and give him presents and yeah. I crocheted him a pikachu. Nobody talked about what we were eating for dinner ahead of time or I just wouldn’t of gone. But when we got there my dad kept asking if my brother wanted to go to Hooters.

Im gonna be honest and just say that it made me feel really uncomfortable. For those of you that don’t know Hooters is this chain restaurant where the whole point is to gawk at the waitresses who are all hot girls wearing white shirts and little orange shorts.

It made me feel really, really uncomfy and bad so I said that they could go inside and I looked and saw there was a bookstore like a 5 minute walk away so I’d go there instead bc I did not want to go. My dad got pissed off and started screaming at me that if I had a problem I could sit in the car. So I said ok, I’ll just sit here. He snatched my phone and screamed that I wouldn’t need my phone to sit here. I said ok. They went in then about 20 minutes later my mom came out to ask me to go inside with them and I said no, I don’t want to go there.
    """ ,
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)
with open('data/tts.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)