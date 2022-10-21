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

input=input('id>')

response = client.get_users_following(id=int(input)).json()

list = {}

for user in response['data']:
    print(user)
    list[user['id']]=[user['name'],user['username']]

list_json=json.dumps(list)

pprint.pprint(list_json)