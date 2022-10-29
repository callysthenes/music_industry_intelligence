import tweepy
import configparser
import pandas as pd
import sys

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy.streaming import Stream
from time import sleep
from random import randint


# API keys corresponding to an academic account
api_key = "4OxfMXFZL9yBDYboGSfcjbFsc"
api_secrets = "Ny9LS2gPD7plQy48c3EpQ3UDvVfqrwvJyZLrAJlgEhQtWz3krW"
access_token =  "1581220096529375238-2Kt6eULOqBD7EvtpqTf4gvU7n69MZ3"
access_secret = "7irLEy7IiGfW72gsh895wntdk3n94upoyXtUMGSo98mch"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPEbiQEAAAAAuuFvB9xcB%2FR4J2RXWNApbAWQ3PY%3DVqvJvvr5WlYDYSfMq5GcZqGGu2gapcfF0ezvJzCWfDaodqSE4L"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
 
try:
    api.verify_credentials()
    #print('Successful Authentication')
    #commented so it doesn't appear in hdfs
except:
    print('Failed authentication')
    
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAPEbiQEAAAAAuuFvB9xcB%2FR4J2RXWNApbAWQ3PY%3DVqvJvvr5WlYDYSfMq5GcZqGGu2gapcfF0ezvJzCWfDaodqSE4L')

# Get tweets that contain the hashtag #badbunny 
# With location is US
# -is:retweet means I don't want retweets
# lang:en is asking for the tweets to be in english
#maximum results are 100, modify this accroding to your api limit!!!!
query = '#theweeknd OR OR theweeknd -is:retweet lang:en place_country: US'

start_time = '2022-01-01T00:00:00Z'
end_time = '2022-10-01T00:00:00Z'

counts = client.get_all_tweets_count(query=query, granularity='day',  start_time=start_time, end_time=end_time)

for count in counts.data:
    print(count)