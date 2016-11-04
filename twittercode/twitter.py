import tweepy

# Unique code from Twitter
access_token = "54789827-a6N4HOqpxAptEZq5yUGw0NyHypRLeCKLmNGkBtaBX"
access_token_secret = "eaiQKEabcdMyliTLiH8PF5pPDeiYqDGmmxi2s1Kz1NoHg"
consumer_key = "RX82rI7hFpzfHxq8SIglyxZqS"
consumer_secret = "Dr3CNJXS8lutOopwSGkPmRC7uRenTGWFfJZHuF63LNyuzDy1Fj"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('UMSI')


for tweet in public_tweets:
	print(tweet.text)
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

