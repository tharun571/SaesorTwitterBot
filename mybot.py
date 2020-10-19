# import tweepy, time, datetime
# import numpy as np
# import pandas as pd
# import csv
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# api = tweepy.API(auth)

# arr = np.array([["0","0","0","0"]])
# arr1 = np.array([["0","0","0","0"]])

# #a and b are used to make sure the already predicted tweets are not replied again


# def likes_predictor(tweetid,userid):

#     #getting the status of the original tweet
#     status = api.get_status(tweetid)

#     #getting the status of the user
#     user = api.get_user(userid)
#     d = status.created_at
#     age = time.time() - (d - datetime.datetime(1970,1,1)).total_seconds()

#     global arr,arr1
#     arr1=np.append(arr1,[[str(tweetid),str(status.favorite_count),str(age),str(user.followers_count)]],axis=0)
    
# def reply_to_tweets():
    
#     #getting the info of the tagged tweet
#     mentions = api.mentions_timeline()
#     for mention in mentions:
#         #getting the tweet id and user id of the original tweet
#         tweetid=mention.in_reply_to_status_id
#         userid=mention.in_reply_to_user_id

#         global list3
        
#         if str(tweetid) not in list3:
#             likes_predictor(tweetid,userid)
#             #api.update_status('@' + mention.user.screen_name +
#             #            'Hi', mention.id)
        

# while True:
#     arr = np.array([["0","0","0","0"]])
#     arr1 = np.array([["0","0","0","0"]])
#     list2 = []
#     with open("test1.csv") as f:
#         list2 = [row.split()[0] for row in f if row != ""] 
#     list3 = []
#     list3 = [list1.split(",")[0] for list1 in list2]
#     for list1 in list2:
#         arr=np.append(arr,[[list1.split(",")[0],list1.split(",")[1],list1.split(",")[2],list1.split(",")[3]]],axis=0) 
#     reply_to_tweets()
#     arr1=np.append(arr,arr1,axis=0)
    
#     np.savetxt('test2.csv', arr1, fmt='%s', delimiter=',')
#     # reader = csv.reader(open("test.csv"))
#     # reader1 = csv.reader(open("test2.csv"))
#     # f = open("test1.csv", "w")
#     # writer = csv.writer(f)

#     # for row in reader:
#     #     writer.writerow(row)
#     # for row in reader1:
#     #     writer.writerow(row)
#     # f.close()

#     # arr1 = np.array([["0","0","0","0"]])
#     time.sleep(15)