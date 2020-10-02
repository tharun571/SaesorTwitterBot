import tweepy, time, datetime
import numpy as np
import pandas as pd
import csv

CONSUMER_KEY = 'mqT85KoatMgF27uILbYGSpV2i'
CONSUMER_SECRET = 'YKiBx5HNXjdg2dpfeShAQ69wncYlKhqtyjT6v7VtlXFbj3kZkr'
ACCESS_KEY = '1307561819410636801-Wf0oCrMu1HkZayyKnbyYAlBkiX7MUb'
ACCESS_SECRET = '1VogIcIiTqbH6LclCVD04sh7jO09CJQdIoo9JY3AoN1FT'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

arr = np.array([[0,0,0,0]],dtype=object)
arr1 = np.array([["0","0","0","0"]])

#a and b are used to make sure the already predicted tweets are not replied again


def likes_predictor(tweetid,userid):

    no_of_likes = np.array([])
    seconds_since_posted = np.array([])
    no_of_followers = np.array([])

    #getting the status of the original tweet
    status = api.get_status(tweetid)

    #getting the status of the user
    user = api.get_user(userid)
    d = status.created_at
    age = time.time() - (d - datetime.datetime(1970,1,1)).total_seconds()

    global arr,arr1
    #arr = np.append(arr,[[tweetid,status.favorite_count,age,user.followers_count]],axis=0)
    arr1=np.append(arr1,[[str(tweetid),str(status.favorite_count),str(age),str(user.followers_count)]],axis=0)
    
    # no_of_likes = np.append(no_of_likes , status.favorite_count)
    # seconds_since_posted = np.append(seconds_since_posted,age)
    # no_of_followers = np.append(no_of_followers,user.followers_count)
    #print(no_of_likes)
    #print(no_of_followers)
    # print(seconds_since_posted)

def reply_to_tweets():
    
    #getting the info of the tagged tweet
    mentions = api.mentions_timeline()
    for mention in reversed(mentions):
        #getting the tweet id and user id of the original tweet
        tweetid=mention.in_reply_to_status_id
        userid=mention.in_reply_to_user_id
        global list3
        if str(tweetid) not in list3:
            likes_predictor(tweetid,userid)
            #api.update_status('@' + mention.user.screen_name +
            #            'Hi', mention.id)
        

while True:
    list2 = []
    with open("test1.csv") as f:
        list2 = [row.split()[0] for row in f if row != ""] 
    list3 = []
    list3 = [list1.split(",")[0] for list1 in list2]
    
    reply_to_tweets()
    
    np.savetxt('test1.csv', arr1, fmt='%s', delimiter=',')
    # reader = csv.reader(open("test.csv"))
    # reader1 = csv.reader(open("test2.csv"))
    # f = open("test1.csv", "w")
    # writer = csv.writer(f)

    # for row in reader:
    #     writer.writerow(row)
    # for row in reader1:
    #     writer.writerow(row)
    # f.close()

    # arr1 = np.array([["0","0","0","0"]])
    time.sleep(15)