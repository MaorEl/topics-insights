import pymongo
from typing import List, Dict, Union
from itertools import chain


MONGO_HOST = "mongodb+srv://amitrechavia:ThisIsNotMyPassword@clusterforbigdatacourse.l0dbxko.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGO_HOST)
db = client['db']
tweets_collection = db['tweets']
users_collection = db['users']


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


def save_tweets(topcis_tweets: Dict[str, List[str]]) -> None:
    """
    save the tweets into the database
    if the topic already exists, append the new tweets to the existing ones
    :param topcis_tweets: A dictionary of key-value pairs where the key is the topic and the value is the tweets
    :return:
    """
    for topic, tweets in topcis_tweets.items():
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
    return {topic: tweets_collection.find_one({"topic": topic}).get('tweets') for topic in topics}


def get_all_topics() -> List[str]:
    return list(set(chain.from_iterable([user.get('topics') for user in users_collection.find()])))


def get_all_users() -> List[str]:
    return [user.get('user_id') for user in users_collection.find()]