import logging

import pandas as pd
import os


class TweeterClient():
    _limit = 2
    _instance = None
    _tweets = None

    def __init__(self):
        if self._instance is None:
            self._instance = self
            current_directory = os.getcwd()
            file_name = "tweets.csv"
            file_path = os.path.join(current_directory, file_name)
            self._tweets = pd.read_csv(file_path)

    def search_tweets(self, topic):
        relevant_tweets = self._tweets['content'][self._tweets['content'].str.contains(topic)]
        tweets_found_counter = len(relevant_tweets)
        logging.info(f'Found {tweets_found_counter} tweets about: {topic}')

        if tweets_found_counter > self._limit:
            relevant_tweets = relevant_tweets.sample(n=self._limit)
            logging.info(f'Filtered to {self._limit} tweets about: {topic}')

        relevant_tweets_dict = relevant_tweets.to_dict()

        return relevant_tweets_dict