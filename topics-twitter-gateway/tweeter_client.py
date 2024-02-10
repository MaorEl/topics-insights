import logging

import pandas as pd
import os


class TweeterClient:
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
        return relevant_tweets