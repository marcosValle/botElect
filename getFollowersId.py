import tweepy
import sys
import json
from pymongo import MongoClient

client = MongoClient()
db = client.twitter

consumer_key = '1Jb78iIqdUujFWyXpEXNvPlqi'
consumer_secret = 'VWQNaKEnW9AiW4Bl7spxDZC8pT27IdIh3sK3MRlddxFSKWLEKM'
access_token = '26650648-w9GU1J0Q8TLbnxMqSPkF8rkIKwXtRlvvncasI79tM'
access_token_secret = 'uihymHbNDjgkVrUU80PzrZ73vhvfHsPXm5jaGZfwfwcR9'

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
