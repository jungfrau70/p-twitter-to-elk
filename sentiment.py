import json
from textblob import TextBlob
import elasticsearch

consumer_key = 'iDmciYm5UDpcqMEww8Hvv5szl'
consumer_secret = '4MeCYwrwxsIw2vflWSlVQdFC7Luv5VDYatl63Uh6ZNGBYqcLwr'
access_token = '104431837-mrtdMgvcDnUIEVx2NPdURthIk37m1PBk1rGWUjSU'
access_token_secret = 'vk9pByLZNBCZ856hBnEvZvFmBGmb7h0PQLxpL74wq1JuC'

# create instance of elasticsearch
config = {
    'host': 'localhost'
}
es = elasticsearch.Elasticsearch([config, ], timeout=300)

import tweepy
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

    # on success
    def on_data(self, data):

        # decode json
        dict_data = json.loads(data)

        # pass tweet into TextBlob
        tweet = TextBlob(dict_data["text"])

        # output sentiment polarity
        print(tweet.sentiment.polarity)

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # output sentiment
        print(sentiment)

        # add text and sentiment info to elasticsearch
        es.index(index="sentiment",
                 doc_type="test-type",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"],
                       "message": dict_data["text"],
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       "sentiment": sentiment})
        return True


if __name__ == '__main__':

    # set twitter keys/tokens
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)

    #for tweet in tweepy.Cursor(api.search, q='realDonaldTrump').items(10):
    #    print(tweet.text)

    # create instance of the tweepy stream
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    # search twitter for "congress" keyword
    myStream.filter(track=['tesla'])
