import tweepy

CONSUMER_KEY = 'mqT85KoatMgF27uILbYGSpV2i'
CONSUMER_SECRET = 'YKiBx5HNXjdg2dpfeShAQ69wncYlKhqtyjT6v7VtlXFbj3kZkr'
ACCESS_KEY = '1307561819410636801-Wf0oCrMu1HkZayyKnbyYAlBkiX7MUb'
ACCESS_SECRET = '1VogIcIiTqbH6LclCVD04sh7jO09CJQdIoo9JY3AoN1FT'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#getting the info of the tagged tweet
metadata=api.mentions_timeline()

#getting the tweet id and user id of the original tweet
tweetid=metadata[0].in_reply_to_status_id
userid=metadata[0].in_reply_to_user_id

#getting the status of the original tweet
status = api.get_status(tweetid)

#getting the status of the user
user=api.get_user(userid)

print(status.__dict__.keys())
print(user.__dict__.keys())