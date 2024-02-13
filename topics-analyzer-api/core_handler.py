from repo.core_repository import CoreRepository
from validator import *

import logging

core_repository = CoreRepository()


def core_sign_up(user_id, topics):
    validate_user_id(user_id)
    validate_topics(topics)
    logging.info(f'Sending sign up request to core-service for user_id: {user_id} and topics: {topics}')
    return core_repository.sign_up(user_id, topics)


def core_analyze(topic):
    validate_topic(topic)
    logging.info(f'Sending analyze request to core-service for topic: {topic}')
    return core_repository.analyze(topic)


def core_visualize(topic):
    validate_topic(topic)
    logging.info(f'Sending visualize request to core-service for topic: {topic}')
    return core_repository.visualize(topic)
