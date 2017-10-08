# Random Video Game Name Twitter-Bot

This is the code behind the twitter-bot [@RandomVGName](https://twitter.com/RandomVGName).

![alt text](https://pbs.twimg.com/media/DLooxxJXkAEEgmP.jpg "Logo")

Mimics part of the functionality of the original Android app: [Random Game Name](https://play.google.com/store/apps/details?id=com.vgname.vgnamegenerator)

![alt text](https://pbs.twimg.com/media/DLl4vEkXkAErA6m.jpg "Logo")

It includes the Python code to:

* Read the random name from a text file **text/names.txt**
* Pick a font at random (from **fonts/**)
* Create a random font color to use
* Convert all this into a .png image using [Pillow](https://python-pillow.org/)
* Send this as a Twitter status with media, using [Tweepy](https://github.com/tweepy/tweepy), at random times

![alt text](https://pbs.twimg.com/media/DLlkIHtXcAAn_Vz.jpg "Logo")

It does not include:

* The complete list of all possible names
* The complete set of fonts used
* System to generate the random names (that is another project).

## How to deploy to Heroku

**TO DO**
