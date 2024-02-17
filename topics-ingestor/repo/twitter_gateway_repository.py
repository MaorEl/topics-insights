import json
import logging
import os

import requests

logging.basicConfig(level=logging.DEBUG)


class TwitterGatewayRepository:

    __instance = None
    TWITTER_GATEWAY_HOST = os.environ.get('TWITTER_GATEWAY_HOST')
    url = f'{TWITTER_GATEWAY_HOST}/twitter-gateway'
    logging.info(f'URL is: {url}')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(TwitterGatewayRepository, cls).__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def fetch_tweets(self,topic):
        URL = self.url + '/search/' + topic

        response = requests.get(URL, params=None, timeout=120)
        response.raise_for_status()

        data: dict = json.loads(response.content.decode('UTF-8'))
        return data
        pass
