import base64
import json
import os
from google.cloud import pubsub_v1
import tweepy

# Configuration Twitter API (Placeholder)
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def fetch_tweets(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    topic_name = "projects/{}/topics/twitter-raw-data".format(os.getenv("GCP_PROJECT_ID"))
    publisher = pubsub_v1.PublisherClient()

    # Search query for "Energy Transition"
    query = "transition énergétique #GCP #DataScience"
    
    # Placeholder logic for fetching tweets
    # In a real scenario, use tweepy.Cursor(api.search_tweets, q=query).items(100)
    
    tweets = [
        {"id": "123", "text": "La transition énergétique est cruciale !", "created_at": "2026-02-02"},
        {"id": "124", "text": "Besoin de plus de panneaux solaires.", "created_at": "2026-02-02"}
    ]

    for tweet in tweets:
        data = json.dumps(tweet).encode("utf-8")
        publisher.publish(topic_name, data)
        print(f"Published tweet {tweet['id']} to Pub/Sub.")
