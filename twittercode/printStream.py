import tweepy
import json

# Unique code from Twitter
access_token = "54789827-a6N4HOqpxAptEZq5yUGw0NyHypRLeCKLmNGkBtaBX"
access_token_secret = "eaiQKEabcdMyliTLiH8PF5pPDeiYqDGmmxi2s1Kz1NoHg"
consumer_key = "RX82rI7hFpzfHxq8SIglyxZqS"
consumer_secret = "Dr3CNJXS8lutOopwSGkPmRC7uRenTGWFfJZHuF63LNyuzDy1Fj"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
def process_or_store(tweet):
	print(tweet.get('user').get('screen_name'))
	print(tweet.get('text').encode('unicode_escape'))
	print(tweet.get('created_at'))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 


for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)


