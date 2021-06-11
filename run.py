from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import pandas as pd
import requests
import flair

load_dotenv()

# read bearer token for authentication
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# setup the API request
endpoint = 'https://api.twitter.com/2/tweets/search/recent'
headers = {'authorization': f'Bearer {BEARER_TOKEN}'}
params = {
    'query': '(tesla OR tsla OR elon musk) (lang:en)',
    'max_results': '100',
    'tweet.fields': 'created_at,lang'
}

response = requests.get(endpoint,
                        params=params,
                        headers=headers)  # send the request
#
# dtformat = '%Y-%m-%dT%H:%M:%SZ'  # the date format string required by twitter
#
# def get_data(tweet):
#     data = {
#         'id': tweet['id_str'],
#         'created_at': tweet['created_at'],
#         'text': tweet['full_text']
#     }
#     return data
#
# df = pd.DataFrame()
# for tweet in response.json()['statuses']:
#     row = get_data(tweet)
#     df = df.append(row, ignore_index=True)
#
# sentiment_model = flair.models.TextClassifier.load('en-sentiment')
#
# sentence = flair.data.Sentence(TEXT)
# sentiment_model.predict(sentence)
#
# # we will append probability and sentiment preds later
# probs = []
# sentiments = []
#
# # use regex expressions (in clean function) to clean tweets
# tweets['text'] = tweets['text'].apply(clean)
#
# for tweet in tweets['text'].to_list():
#     # make prediction
#     sentence = flair.data.Sentence(tweet)
#     sentiment_model.predict(sentence)
#     # extract sentiment prediction
#     probs.append(sentence.labels[0].score)  # numerical score 0-1
#     sentiments.append(sentence.labels[0].value)  # 'POSITIVE' or 'NEGATIVE'
#
# # add probability and sentiment predictions to tweets dataframe
# tweets['probability'] = probs
# tweets['sentiment'] = sentiments
#
#
# # we use this function to subtract 60 mins from our datetime string
# def time_travel(now, mins):
#     now = datetime.strptime(now, dtformat)
#     back_in_time = now - timedelta(minutes=mins)
#     return back_in_time.strftime(dtformat)
#
#
# now = datetime.now()  # get the current datetime, this is our starting point
# last_week = now - timedelta(days=7)  # datetime one week ago = the finish line
# now = now.strftime(dtformat)  # convert now datetime to format for API
#
# df = pd.DataFrame()  # initialize dataframe to store tweets
#
# df = pd.DataFrame()  # initialize dataframe to store tweets
#
# while True:
#     if datetime.strptime(now, dtformat) < last_week:
#         # if we have reached 7 days ago, break the loop
#         break
#     pre60 = time_travel(now, 60)  # get 60 minutes before 'now'
#     # assign from and to datetime parameters for the API
#     params['start_time'] = pre60
#     params['end_time'] = now
#     response = requests.get(endpoint,
#                             params=params,
#                             headers=headers)  # send the request
#     now = pre60  # move the window 60 minutes earlier
#     # iteratively append our tweet data to our dataframe
#     for tweet in response.json()['data']:
#         row = get_data(tweet)  # we defined this function earlier
#         df = df.append(row, ignore_index=True)