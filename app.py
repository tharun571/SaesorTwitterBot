import tweepy
import pickle
from config import *
import json
import schedule
import time

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# it is used keep track of the replied tweets
tweet_id_list=[]

def predict_likes(followers):

    regressor = pickle.load(open("twitter_bot.sav", 'rb'))
    likes_count = regressor.predict([[3000, followers]])

    return likes_count


def reply_to_the_tweet(tweetid, likes_count):
    
    if tweetid not in tweet_id_list:
        text = "Hello! Predicted likes within 50 minutes is - "+str(likes_count)

        api.update_status(text, in_reply_to_status_id=tweetid,
                        auto_populate_reply_metadata=True)

        print("success")
        tweet_id_list.append(tweetid)
    else:
        print("already predicted")

def start():

    for mention in tweepy.Cursor(api.mentions_timeline).items():

        # getting the mentioned tweet

        json_str=json.dumps(mention._json)
        parsed = json.loads(json_str)

        # Below code is to get the followers and user information of the original tweet using the tweet id
        user=api.get_user(parsed["entities"]["user_mentions"][0]["id"])
        json_str1=json.dumps(user._json)
        parsed1=json.loads(json_str1)

        #parsed1 is the user info object

        val=predict_likes(parsed1["followers_count"])
        reply_to_the_tweet(parsed["id"],val)
        
        # sleeping in order to avoid the rate limits
        time.sleep(60)


# using schedule for running the code every one hour

schedule.every(1).hour.do(start)
while True:
    schedule.run_pending()
    time.sleep(1)

    