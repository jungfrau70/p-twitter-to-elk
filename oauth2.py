import tweepy
import pandas as pd


if __name__ == '__main__':
    # OAuth 2
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)
    for tweet in tweepy.Cursor(api.search, q='realDonaldTrump').items(10):
        print(tweet.text)