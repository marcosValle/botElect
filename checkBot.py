import botometer
from pymongo import MongoClient
import json
from termcolor import colored

client = MongoClient('localhost:27017')
db = client.twitter

#def checkSeenId(userId, db):
#    if db.bots.find(userId)


pages = db.bolsonaro.find()
ids = []
for p in pages:
    ids += list(p["ids"])

mashape_key = "4DIsgsa2cFmshln8tmCfVHtKAZwFp1wQS8VjsnxEpy45JnTxvz"
twitter_app_auth = {
    'consumer_key': 'VUd3ocqPL98hWHBKrZfiqn9Nb',
    'consumer_secret': 'aWKOW8rVjS9yqrp2DJLDxhWmkUaxF5UgmGwWwHuSJzv6iXN6Np',
    'access_token': '26650648-rNmi8yL4fDXZCS3mCexYgHRNyTYBeEm5pNdn3NLIt',
    'access_token_secret': 'BJLx3pOq4PzS4xdJOvXZhBXic26ZsfLXeOL6nCZVqP9lu',
  }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)


for result in bom.check_accounts_in(ids):
    try:
        cap = result[1]['cap']['universal']

        if cap >= 0.7:
            print(colored(str(result[1]['user']['screen_name']) + ": " + str(cap) + " [BOT]", 'red'))
            bot = {
                    'handle': 'Bolsonaro',
                    'id': result[0],
                    'bot': 1
                    }
        else:
            print(colored(str(result[1]['user']['screen_name']) + ": " + str(cap) + " [HUMAN]", 'green'))
            bot = {
                    'handle': 'Bolsonaro',
                    'id': result[0],
                    'bot': 0
                    }

        db.bots.insert_one(bot)
    except Exception as e:
        print(colored("### Unable to identify ###\n{}".format(result), 'yellow'))
