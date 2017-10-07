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

minMins = 10
maxMins = 60*12

tmpfile = "logo.png"
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

while True:
    line = choice(f).rstrip()
    randomimage.imageFromText(line,tmpfile)
    api.update_with_media(tmpfile,line)
    #print(line)
    time.sleep(60*randint(minMins,maxMins))
    os.remove(tmpfile)
