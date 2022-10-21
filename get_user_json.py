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

input=input('id or username>')

if input.isdigit():
    response = client.get_user(id=int(input)).json()
else:
    response = client.get_user(username=input).json()

pprint.pprint(response)
