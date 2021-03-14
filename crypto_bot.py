# -*- coding: utf-8 -*-
import json
import tweepy
import datetime 
from requests_oauthlib import OAuth1Session


def get_keys():     
        data = 'keys.json'
        with open(data,'r') as f:
            keys = json.load(f)
        return keys

keys = get_keys()
consumer_key = keys['api_key']
consumer_secret = keys['api_key_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

filters = '-filter:retweets AND -filter:replies AND -filter:mentions'
search = 'Avax NFT minted' + filters
nTweets = 5

for tweet in tweepy.Cursor(api.search,search).items(nTweets):
    if(tweet.favorited == True and tweet.retweeted == True):               
        print('Tweet already retweeted and liked')      
    elif(tweet.favorited == True and tweet.retweeted == False):
        try:            
            tweet.retweet()            
        except tweepy.TweepError as e:
            print (e.reason)   
    elif(tweet.favorited == False and tweet.retweeted == True):
        try:           
            tweet.favorite()            
        except tweepy.TweepError as e:
            print (e.reason) 
    else:
        try:            
            tweet.retweet()
            tweet.favorite()
        except tweepy.TweepError as e:
            print(e.reason)
    