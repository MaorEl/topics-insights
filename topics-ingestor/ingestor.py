import logging

from db import mongo_client
from repo.twitter_gateway_repository import IngestorRepository


class DataIngestor:
    db_client = None

    def __init__(self):
        self.db_client = mongo_client
        self.ingestor_repo = IngestorRepository()

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
                tweets = self.ingestor_repo.fetch_tweets(topic)

                if (tweets is None) or (len(tweets) == 0):
                    logging.info(f'No tweets for topic: {topic}')
                    continue
                else:
                    # todo maor - parse tweets somehow
                    self.db_client.save_tweets(topic, str(tweets))
                    logging.info(f'Ingested {len(tweets)} tweets for topic: {topic}')
            except Exception as e:
                logging.error(f'Error while ingesting tweets for topic: {topic}. Error: {e}')
