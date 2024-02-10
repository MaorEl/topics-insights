import redis
from typing import List, Dict


def sign_up(user_id: str, topics: List[str]) -> None:
    """
    register a new user into the database with the given topics
    raise an error if the user_id already exists
    :param user_id:
    :param topics:
    :return:
    """
    raise NotImplementedError()


def save_tweets(topcis_tweets: Dict[str, List[str]]) -> None:
    """
    save the tweets into the database
    if the topic already exists, append the new tweets to the existing ones
    :param tweets: A dictionary of key-value pairs where the key is the topic and the value is the tweets
    :return:
    """
    raise NotImplementedError()


def get_tweets(topics: List[str]) -> Dict[str, List[str]]:
    """
    get the tweets for the given topics
    :param topics:
    :return: A dictionary of key-value pairs where the key is the topic and the value is the tweets
    """
    raise NotImplementedError()



if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')
    print(r.get('foo'))
    r.delete('foo')
    print(r.get('foo'))
    r.set('foo', 'bar')
    r.expire('foo', 5)
