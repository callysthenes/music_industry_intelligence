#!/usr/bin/python3

import tweepy
import argparse
import json

# usage: TwitterRTI.py [-h] --terms TERMS
#
# optional arguments:
#   -h, --help     show this help message and exit
#   --terms TERMS  Search terms to get tweets of interest

class MDATwitter(tweepy.Stream):

    def on_data(self, raw_data):
        print(raw_data)
        
def main(terms):
    
    # 1. Setup Tweepy to use our Twitter App settings.
    consumer_key = "your consumer_key"
    consumer_secret = "your consumer_secret"
    access_token = "your access_token"
    access_token_secret = "your access_token_secret"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    # 2. Setup Tweety to ingest tweets in real-time (stream data)
    stream = MDATwitter(consumer_key, consumer_secret, access_token, access_token_secret)
    
    # 3. Start streaming data from Twitter
    stream.filter(track=terms.split(","))
    stream.sample()

if __name__ == "__main__":
    # 1. Setup arguments parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--terms", help="Search terms to get tweets of interest", required=True)
    args = parser.parse_args()
    # 2. Call the main function with the search terms.
    main(args.terms)
    