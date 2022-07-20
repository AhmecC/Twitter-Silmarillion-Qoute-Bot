import tweepy as tweepy
import random
from time import sleep

# -------------------- CONNECT TO TWITTER API -------------------- #
API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

authenticator = tweepy.OAuthHandler(API_KEY, API_SECRET)
authenticator.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(authenticator, wait_on_rate_limit=True)

for i in range(0,4):
    sleep(60)
    with open("Sentences.txt", "r+") as file:
        qoutes = file.readlines()
        CHOSEN = random.choice(qoutes)
        qoutes.remove(CHOSEN)  
    # Randomly chooses a line

    with open("Sentences.txt","w+") as file:
        for i in qoutes:
            file.write(i)
    # removes chosen line from the file (to avoid duplicates)
        
        
# -------------------- FIX QOUTE UP FURTHER -------------------- #
    A = ""
    for char in CHOSEN:
        if char in r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?,!:;.()-"\' ':
            A += char
    # As Sentences.txt is not wholly clean, this takes unwanted characters out

    B = A.split()
    C = " ".join(B)  # This fixes the issue of spacing as seen in Sentences.txt

    twt_1 = []
    twt_2 = []
    if len(C) > 280:
        D = C.split()
        count = 0
        for i in D:
            count += len(i)+1
            if count <= 260:
                twt_1.append(i)
            if count > 260:
                twt_2.append(i)

        twt_1 = " ".join(twt_1) + " - "
        twt_2 = "- " + " ".join(twt_2)
        # If the quote exceeds 280 characters its split up and formated accordingly

    if len(C) < 280:
        api.update_status(status = f"'{C}'")
        # Posts a tweet

    if len(C) > 280:
        FIRST = api.update_status(status = f"'{twt_1}'")
        SECOND = api.update_status(status = f"'{twt_2}'", in_reply_to_status_id = FIRST.id, auto_populate_reply_metadata=True)
        # Posts a thread with the whole qoute
    
    sleep(10800) #Tweets every 3 hours
