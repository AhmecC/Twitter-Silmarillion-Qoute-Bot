import tweepy
import schedule
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


# -------------------- CREATE/SEND/INTERACT WITH TWEETS -------------------- #
def formatter(CHOSEN):
    """Ensures the spacing of the sentence is correct"""
    text = CHOSEN.split(" ")
    text = " ".join(text)
    quote = f"'{text[:-1]}'"
    return quote

def main():
    """Determines the quote, puts through functions and tweets out"""
    CHOICE = f"Chap {random.randint(1,28)}"  # Chooses Chap where Quote will come from

    with open(f"Silmarillion/{CHOICE}/{CHOICE}.txt", encoding="utf-8") as file:
        quotes = file.readlines()
        CHOSEN = random.choice(quotes)
        quotes.remove(CHOSEN)  # Chooses a Quote from specified chapter and then deletes it from file
    with open(f"Silmarillion/{CHOICE}/{CHOICE}.txt","w", encoding="utf-8") as f:
        for i in quotes:
            f.write(i)

    names = ["Durin", "Elrond", "Galadriel", "Númenor", "Lindon", "Isildur", "Gil-galad", "Elendil", "Finrod", "Ar-Pharazôn", "Sauron"] 
      hash = ["#TheRingsOfPower", "#amazon", "#LordoftheRings", "#tolkien"]  # If relevant name is found in quote is created into a hashtag
    for i in names:
        if i in CHOSEN:
            hash.append(f"#{i}")
    CHOSEN = formatter(CHOSEN)
    a = imageCreator(CHOSEN, CHOICE)  # Creates the image itself
    media = api.media_upload("result.png")
    hashtags = " ".join(hash)
    tweet = api.update_status(status=hashtags, media_ids=[media.media_id])
    api.create_favorite(id=tweet.id)
    
    
# -------------------- SCHEDULER -------------------- #
def checker():
    tp = (int(time.time()) % 86400) + 60*60  # Adjusts for time discrepancy
    times = [28800,36000,43200,50400,57600,64800,72000]

    if 28700 <= tp <= 72100: # if between 8am-8pm
        for i in times:
            if i-60 <= tp <= i+60:
                main()

while True:
    time.sleep(120)  # Every 120s check if time is correct
    checker()
