import tweepy
import sys
import json
from pymongo import MongoClient

client = MongoClient()
db = client.twitter

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    handle = 'jairbolsonaro'
    c = tweepy.Cursor(api.followers_ids, id = handle)

    for page in c.pages():
        p = {
                "handle": handle,
                "ids": page
                }

        print(p)
        try:
            db.bolsonaro.insert_one(p)
        except Exception as e:
            print(e)

except tweepy.TweepError as e:
    print("tweepy.TweepError={}".format(e))
except Exception as e:
    print("Error: {}".format(e))
