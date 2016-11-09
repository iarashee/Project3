# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

#print("""No output necessary although you 
#	can print out a success/failure message if you want to.""")

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

api.update_with_media("twittertest.jpg", "#UMSI-206 #Proj3")

print ("done")