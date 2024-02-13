import logging

from db import mongo_client
from repo.twitter_gateway_repository import TwitterGatewayRepository


class DataIngestor:
    db_client = None

    def __init__(self):
        self.db_client = mongo_client
        self.twitter_gateway_repo = TwitterGatewayRepository()

    def ingest_tweets(self):
        logging.info('Ingesting tweets from Twitter...')
        topics = self.db_client.get_all_topics()

        if topics is None or (len(topics)) == 0:
            logging.warning('No topics to ingest tweets for')
            return

        logging.info('Handling topics: {}'.format(topics))

        for topic in topics:
            try:
                logging.info(f'Ingesting tweets topic: {topic}')
                tweets = self.twitter_gateway_repo.fetch_tweets(topic)
                if (tweets is None) or (len(tweets) == 0):
                    logging.info(f'No tweets for topic: {topic}')
                    continue
                else:
                    tweets_by_topic_dict = {topic: [tweet['tweet_text'] for tweet in tweets]}
                    self.db_client.save_tweets(tweets_by_topic_dict)
                    logging.info(f'Ingested {len(tweets_by_topic_dict)} tweets for topic: {topic}')
            except Exception as e:
                logging.error(f'Error while ingesting tweets for topic: {topic}. Error: {e}')
