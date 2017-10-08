import tweepy, time, sys
import randomimage
import os
from random import choice, randint

argfile = str(sys.argv[1])

# add your own credentials
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

minMins = 10     # 10 minutes is the min wait time
maxMins = 60*4   # max wait time is 4 hours

tmpfile = "logo.png"
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

while True:
    line = choice(f).rstrip()
    randomimage.imageFromText(line,tmpfile)
    api.update_with_media(tmpfile,line)
    print(line)
    waitTime = randint(minMins,maxMins)
    print("Waiting " + str(waitTime) + " minutes")
    time.sleep(60*waitTime)
    os.remove(tmpfile)
