import tweepy
import random
from time import sleep
from imageCreator import imageCreator  # Imports class that creates the image


# -------------------- CONNECT TO TWITTER API -------------------- #
API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

authenticator = tweepy.OAuthHandler(API_KEY, API_SECRET)
authenticator.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(authenticator, wait_on_rate_limit=True)

def formatter(CHOSEN):
    text = CHOSEN.split(" ")
    text = " ".join(text)
    quote = f"'{text[:-1]}'"
    return quote

START = True
while START:
    CHOICE = f"Chap {random.randint(1,28)}"

    with open(f"Silmarillion/{CHOICE}/{CHOICE}.txt", encoding="utf-8") as file:
        quotes = file.readlines()
        CHOSEN = random.choice(quotes)
        quotes.remove(CHOSEN)

    with open(f"Silmarillion/{CHOICE}/{CHOICE}.txt","w", encoding="utf-8") as f:
        for i in quotes:
            f.write(i)


    names = ["Durin", "Elrond", "Galadriel", "Númenor", "Lindon", "Isildur", "Gil-galad", "Elendil", "Finrod", "Ar-Pharazôn"] 
    hash = ["#RingsOfPower", "#lotr",]  # If relevant name is found in quote is created into a hashtag
    for i in names:
        if i in CHOSEN:
            hash.append(f"#{i}")


    CHOSEN = formatter(CHOSEN)
    
    a = imageCreator(CHOSEN, CHOICE)
    print("Generated")
    print(hash)

    media = api.media_upload("result.png")
    hashtags = " ".join(hash)
    tweet = api.update_status(status=hashtags, media_ids=[media.media_id])
    api.create_favorite(id=tweet.id)

    sleep(10800)  # Every 3 Hours
