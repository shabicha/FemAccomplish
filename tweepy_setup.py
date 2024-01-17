# Importing Tweepy
import tweepy
from credentials import api_key
from credentials import api_secret
from credentials import bearer_token
from credentials import access_token
from credentials import access_token_secret
from webscrapper import forbes_data


 #limitations for this project here: https://superface.ai/blog/twitter-api-new-plans


# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


#Sample tweet given webscrappers list 
title = forbes_data[3]['title']
link = forbes_data[3]['link']
tweet_text = f"{title}\n{link}"

# Creating a tweet to test the bot
client.create_tweet(text=tweet_text)

