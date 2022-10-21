import json
import os
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


def metrics_home_json(client: tweepy.Client):
    return client.get_home_timeline(
        exclude=['retweets', 'replies'],
        tweet_fields=['created_at','author_id','public_metrics'],
        user_fields=['name','username'],
        expansions=['author_id']
    ).json()


def extract_users_list(home: json):
    ids = []
    for tweet in home['data']:
        id = tweet['author_id']
        if not (id in ids):
            ids.append(id)
    return ids


def get_users_dict(client: tweepy.Client, ids:list):
    response = client.get_users(ids=ids).json()
    users_dict = {}
    for user in response['data']:
        users_dict[user['id']] = [user['name'], user['username']]
    return users_dict


def trans_users_home_json(home: json):
    ids = extract_users_list(home)
    users_dict = get_users_dict(client, ids)
    for tweet in home['data']:
        tweet['name'] = users_dict[tweet['author_id']][0]
        tweet['username'] = users_dict[tweet['author_id']][1]
    return home


response = metrics_home_json(client)

# response = trans_users_home_json(response)

pprint.pprint(response)

with open('output.json', 'w') as f:
    json.dump(response, f, indent=4)