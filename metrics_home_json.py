import os
import json
import pprint
import tweepy
from requests import Response

client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET'],
    return_type=Response
)

response = client.get_home_timeline(
    exclude=['retweets', 'replies'],
    tweet_fields=['public_metrics']
    ).json()

pprint.pprint(response)
