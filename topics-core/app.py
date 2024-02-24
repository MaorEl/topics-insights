import logging
from datetime import datetime

import openai
import pandas as pd
from flask import Flask, request
from db import mongo_client
import json

# https://stackoverflow.com/questions/73745245/error-using-matplotlib-in-pycharm-has-no-attribute-figurecanvas
import matplotlib
matplotlib.use('TkAgg')
matplotlib.use('agg')
import matplotlib.pyplot as plt
import os

from model.topic_rate import TopicRate

logging.basicConfig(level=logging.INFO)
OPEN_AI_KEY = os.environ.get('OPENAI_API_KEY').split('\n')[0]
logging.info(f'OpenAI key: {OPEN_AI_KEY}')
openai.api_key = OPEN_AI_KEY
app = Flask(__name__)


@app.errorhandler(ValueError)
def handle_value_error(e):
    return f'Error occurred: {str(e)}', 500


@app.route('/signUp')
def sign_up():
    """
    sign up a new user with the given topics
    call /signUp?user_id=my_user_id&topics=topic1,topic2,topic3
    """
    args = request.args
    user_id = args['user_id']
    topics = args['topics'].split(',')
    mongo_client.sign_up(user_id, topics)
    return f"user {user_id} starting to follow topics {topics}"


def _find_number_from_text(text: str) -> int:
    """
    find the first number from the given text, if no number is found, return 1
    """
    import re
    pattern = r'\d+'
    match = re.search(pattern, text)
    if match:
        number = match.group()
        return int(number)
    else:
        return 1


@app.route('/analyze')
def analyze():
    """
    analyize the given topic,
    call /analyze?topic=topic_name
    """
    topic = request.args['topic']
    tweets = mongo_client.get_tweets(topic)

    if tweets is None:
        return f"No tweets for topic {topic}"

    tweets_for_topic = tweets[topic]

    if not tweets_for_topic:
        return f"No tweets for topic {topic}"

    if len(tweets_for_topic) > 5:
        logging.info("Filtering last 5 tweets")
        tweets_for_topic = tweets_for_topic[-5:]

    prompt = (f"Give a number between 1 and 10 to describe the sentiment level of people according to the tweets. "
              f"10 is super positive and 1 is super negative. Tweets: {tweets_for_topic}")
    content = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0).choices[0].message.content
    rate = _find_number_from_text(content)
    topic_rate = TopicRate(rate=rate, time=datetime.now())
    encoded_data = topic_rate_encoder(topic_rate)
    mongo_client.save_tweet_rate(topic, encoded_data)
    return f'{topic} sentiment level is: {rate}'


def topic_rate_encoder(obj):
    if isinstance(obj, TopicRate):
        return {'time': obj.time, 'rate': obj.rate}
    return obj


@app.route('/visualize')
def visualize():
    """
    visualize the level of excitement for the tweets of the given topic
    the X axis is the tweet number and the Y axis is the insight satisfaction
    call /visualize?topic=topic_name
    if you want to see the graph in your machine, save the returned values as var named 'data' and run the following code:

    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.DataFrame(json.loads(data))
    plt.plot(df['X'], df['Y'])
    plt.xlabel('tweet number')
    plt.ylabel('insight satisfaction')
    plt.title('tweet to satisfaction graph')
    plt.grid(True)
    plt.show()


    """
    topic = request.args['topic']
    insights = mongo_client.get_tweets_rates(topic)

    if insights is None:
        return f"No insights for topic {topic}"

    try:
        topic_rates = [TopicRate(time=entry['time'], rate=int(entry['rate'])) for entry in insights]

        # Convert TopicRate objects to a Pandas DataFrame
        df = pd.DataFrame([(tr.time, tr.rate) for tr in topic_rates], columns=['time', 'rate'])

        # Sort DataFrame by time
        df.sort_values(by='time', inplace=True)

        # Plot the data
        plt.plot(df['time'], df['rate'])
        plt.title(f'Topic {topic} Sentiment Level Over Time')
        plt.xlabel('Time')
        plt.ylabel('Sentiment Level')
        plt.xticks(rotation=45)
        plt.show(block=False)
        plt.pause(2)
        plt.close()
        json_results = df[['time', 'rate']].to_json(orient='records', date_format='iso', default_handler=str)

        parsed_json = json.loads(json_results)
        return parsed_json
    except Exception as e:
        return f"Error occurred: {str(e)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
