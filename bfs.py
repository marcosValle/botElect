import tweepy
import csv
import time

consumer_key=""
consumer_secret=""
access_token="-"
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

startAccount = 'LulaOficial'
visited=[]

def writeToFile(fpath, vertex1, vertex2):
    with open(fpath, 'a+') as f:
        f.write(vertex1+','+vertex2+'\n')

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

def BFS(node, depth):
    visited.append(node)
    users = tweepy.Cursor(api.followers, screen_name=node).items()

    for user in limit_handled(users):
        if depth<3:
            if user not in visited:
                visited.append(node)
                print(node + ", " + user.screen_name)
                BFS(user.screen_name, depth+1)
            else:
                print(node+' already seen')
        #writeToFile('followers.csv', currAcc, user.screen_name)

BFS(startAccount, 0)
