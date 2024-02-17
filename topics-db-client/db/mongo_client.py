import os

import pymongo
from typing import List, Dict, Union
from itertools import chain
MONGO_HOST = os.environ.get('DB_HOST')
MONGO_USERNAME = os.environ.get('DB_USERNAME')
MONGO_PASSWORD = os.environ.get('DB_PASSWORD')

MONGO_HOST = f'mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGO_HOST)
db = client['db']
tweets_collection = db['tweets']
users_collection = db['users']
tweets_rates_collection = db['insights']


def save_tweet_rate(topic, rate) -> None:
    """
    save the tweet rate into the database for the given topic
    """
    tweets_rates_collection.update_one(
        {"topic": topic},
        {"$push": {"rates": {"$each": [rate]}}},
        upsert=True
    )


def get_tweets_rates(topic) -> List[str]:
    """
    get the insights for the given topic
    """
    return tweets_rates_collection.find_one({"topic": topic}).get('rates')


def sign_up(user_id: str, topics: List[str]) -> None:
    """
    register a new user into the database with the given topics
    if the user_ud exists, append the new topics to the existing user
    :param user_id:
    :param topics:
    :return:
    """
    users_collection.update_one(
        {"user_id": user_id},
        {"$addToSet": {"topics": {"$each": topics}}},
        upsert=True
    )


def save_tweets(tweets_by_topic: Dict[str, List[str]]) -> None:
    """
    save the tweets into the database
    if the topic already exists, append the new tweets to the existing ones
    :param tweets_by_topic: A dictionary of key-value pairs where the key is the topic and the value is the tweets
    :return:
    """
    for topic, tweets in tweets_by_topic.items():
            tweets_collection.update_one(
                {"topic": topic},
                {"$addToSet": {"tweets": {"$each": tweets}}},
                upsert=True
            )


def get_tweets(topics: Union[List[str], str]) -> Dict[str, List[str]]:
    """
    get the tweets for the given topics
    :param topics:
    :return: A dictionary of key-value pairs where the key is the topic and the value is the tweets
    """
    if isinstance(topics, str):
        topics = [topics]

    tweets_dict = {}
    for topic in topics:
        result = tweets_collection.find_one({"topic": topic})
        tweets = result.get('tweets') if result else []
        tweets_dict[topic] = tweets

    return tweets_dict
    # fix this method to work with none result for the find_one method????



def get_all_topics() -> List[str]:
    return list(set(chain.from_iterable([user.get('topics') for user in users_collection.find()])))


def get_all_users() -> List[str]:
    return [user.get('user_id') for user in users_collection.find()]

