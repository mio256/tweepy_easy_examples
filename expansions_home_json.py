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
        expansions=['author_id','attachments.media_keys'],
        user_fields=['name','username','profile_image_url','url'],
        media_fields=['url']
    ).json()


response = metrics_home_json(client)

pprint.pprint(response)

with open('output.json', 'w') as f:
    json.dump(response, f, indent=4)