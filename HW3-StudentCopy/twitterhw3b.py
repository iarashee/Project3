# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

#Unique Account Info
access_token = 
access_token_secret = 
consumer_key = 
consumer_secret = 

#Normal Auth
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#Search Term
print ("\n\n**START**\n\n")
searched_tweets = api.search("'Crooked' @realDonaldTrump")

l_subjectivity = []
l_polarity = []

for tweet in searched_tweets:
	y = TextBlob(tweet.text)
	l_subjectivity.append(y.sentiment.subjectivity)
	l_polarity.append(y.sentiment.polarity)
	print (tweet.text)

avg_subjectivity = sum(l_subjectivity) / len(l_subjectivity)
avg_polarity = sum(l_polarity) / len(l_polarity)

print("\nAverage subjectivity is", avg_subjectivity)
print("Average polarity is", avg_polarity)
print ("\n\n**END**\n\n")
