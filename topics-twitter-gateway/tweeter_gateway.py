import logging
from tweeter_client import TweeterClient
from model.tweet import Tweet

class TweeterGateway:
    _instance = None
    _client = None
    _limit = 3

    def __init__(self):
        if self._instance is None:
            self._instance = self
            self._client = TweeterClient()

    def search(self, topic):
        global relevant_tweets
        logging.info(f'Searching for tweets about: {topic}')
        tweets_result = self._client.search_tweets(topic)
        tweets_found_counter = len(tweets_result)
        logging.info(f'Found {tweets_found_counter} tweets about: {topic}')

        if tweets_found_counter > self._limit:
            tweets_result = tweets_result.sample(n=self._limit)
            logging.info(f'Filtered to {self._limit} tweets about: {topic}')

        relevant_tweets_dict = tweets_result.to_dict()
        ret_val = []
        for key in relevant_tweets_dict.keys():
            tweet = Tweet(tweet_id=key, tweet_text=relevant_tweets_dict[key])
            ret_val.append(tweet)

        return ret_val
