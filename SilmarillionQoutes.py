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

while True:
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
    if len(C) > 260:
        D = C.split()
        count = 0
        for i in D:
            count += len(i)+1
            if count <= 250:
                twt_1.append(i)
            if count > 250:
                twt_2.append(i)

        twt_1 = " ".join(twt_1) + " - "
        twt_2 = "- " + " ".join(twt_2)
        # If the quote exceeds 280 characters its split up and formated accordingly
        
    if len(C) < 260:
        single = api.update_status(status = f"'{C}'\n\n#RingsOfPower #lotr")
        api.create_favorite(id=single.id)  # Posts and then likes own tweet

    if len(C) >= 260:
        FIRST = api.update_status(status = f"'{twt_1} '")
        SECOND = api.update_status(status = f"'{twt_2}'\n\n#RingsOfPower #lotr", in_reply_to_status_id = FIRST.id, auto_populate_reply_metadata=True)
        api.create_favorite(id=FIRST.id)
        api.create_favorite(id=SECOND.id)
    
    sleep(10800) #Tweets every 3 hours
