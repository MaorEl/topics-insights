import openai
from flask import Flask, request
from db import mongo_client
import numpy as np
import json

# https://stackoverflow.com/questions/73745245/error-using-matplotlib-in-pycharm-has-no-attribute-figurecanvas
import matplotlib
matplotlib.use('TkAgg')
matplotlib.use('agg')
import matplotlib.pyplot as plt
import os
openai.api_key = os.environ.get('OPENAI_API_KEY')
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

    prompt = f"Give a number between 1 and 10 to describe the excitement level of people according to the tweets {tweets_for_topic}"
    content = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0).choices[0].message.content
    rate = _find_number_from_text(content)
    mongo_client.save_tweet_rate(topic, rate)
    str_tweets_for_topic = '  \n'.join(tweets_for_topic)
    return '  \n'.join(['we asked what chat-gpt thinks about the tweets:', str_tweets_for_topic, f'it answered: {content}'])


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
        x_values = range(1, len(insights) + 1)  # Generate x values from 1 to length of the list
        plt.plot(x_values, insights, marker='o', linestyle='-')
        plt.xlabel('tweet number')
        plt.ylabel('insight satisfaction')
        plt.title('tweet to satisfaction graph')
        plt.grid(True)
        plt.xticks(np.arange(min(x_values), max(x_values) + 1, 1))
        plt.show(block=False)
        plt.pause(2)
        plt.close()
        return json.dumps({"x": list(x_values), "y": insights})
    except Exception as e:
        return f"Error occurred: {str(e)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
