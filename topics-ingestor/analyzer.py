import logging

from db import mongo_client
from repo.core_repository import CoreRepository


class DataAnalyzer:
    db_client = None

    def __init__(self):
        self.db_client = mongo_client
        self.core_repo = CoreRepository()

    def analyze_topics(self):
        logging.info('Analyze Topics...')
        topics = self.db_client.get_all_topics()

        if topics is None or (len(topics)) == 0:
            logging.warning('No topics to analyze tweets for')
            return

        logging.info('Handling topics: {}'.format(topics))

        for topic in topics:
            try:
                logging.info(f'Analyze tweets topic: {topic}')
                analyze_results = self.core_repo.analyze(topic)
                if analyze_results is None:
                    logging.info(f'No analyze results for topic: {topic}')
                    continue
                else:
                    logging.info(f'Analyze results is: {analyze_results} for topic: {topic}')
            except Exception as e:
                logging.error(f'Error while analyze tweets for topic: {topic}. Error: {e}')
