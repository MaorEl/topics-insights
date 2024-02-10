import logging
from tweeter_client import TweeterClient


class TweeterGateway:
    _instance = None
    _client = None

    def __init__(self):
        if self._instance is None:
            self._instance = self
            self._client = TweeterClient()

    def search(self, topic):
        logging.info(f'Searching for tweets about: {topic}')
        tweets_result = self._client.search_tweets(topic)
        return tweets_result
