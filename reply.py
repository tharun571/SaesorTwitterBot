import tweepy, time, datetime
import numpy as np
import pandas as pd
import csv



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()
for mention in mentions:
    #getting the tweet id and user id of the original tweet
    tweetid=mention.in_reply_to_status_id
    userid=mention.in_reply_to_user_id
    api.update_status('@' + mention.user.screen_name +
                       'Hi', mention.id)
        
        
        
           
           