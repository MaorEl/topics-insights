import logging
from db import mongo_client

USERS = ['user1', 'user2', 'user3']


def validate_user_id(user_id: str):
    logging.info(f'Validating user_id: {user_id}')

    if not user_id:
        raise ValueError('user_id is empty')

    if len(user_id) > 50:
        raise ValueError('user_id is too long')

    if user_id in USERS:
        raise ValueError('user_id already exists')
    pass


def validate_topics(topics: str):
    logging.info(f'Validating topics: {topics}')

    if not topics:
        raise ValueError('topics is empty')
    joined_topics: [] = topics.join(',')

    if not joined_topics:
        raise ValueError('topics is empty')

    if len(joined_topics) > 50:
        raise ValueError('topics is too long. Max 50 topics are allowed')
    pass


def validate_topic(topic: str):
    logging.info(f'Validating topic: {topic}')

    topics = mongo_client.get_all_topics()

    if topics is None or (len(topics)) == 0:
        logging.warning('No topics to ingest tweets for')
        raise ValueError('No topics to ingest tweets for')

    if topic not in topics:
        raise ValueError('topic does not exist. First sign up!')

    if not topic:
        raise ValueError('topic is empty')
    if len(topic) > 15:
        raise ValueError('topic is too long. Max 15 chars for topic are allowed')
    pass
