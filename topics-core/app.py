import openai
from flask import Flask, request
from db import mongo_client
import matplotlib.pyplot as plt
import numpy as np

openai.api_key = "insert_here_your_openai_api_key"
app = Flask(__name__)


@app.route('/signUp')
def sign_up():
    """
    sign up a new user with the given topics
    call /analyze?signUp=user_id&topics=topic1,topic2,topic3
    """
    args = request.args
    user_id = args.get('user_id')
    topics = args.get('topics').split(',')
    mongo_client.sign_up(user_id, topics)


def find_number_from_text(text: str) -> int:
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
    topic = request.args.get('topic')
    tweets_for_topic = mongo_client.get_tweets(topic)[topic]
    rate = find_number_from_text(openai.ChatCompletion.create(
        engine="gpt-3.5-turbo",
        messages=f"give a number between 1 and 10 which "
                 f"describes what is the excitement level of people acordding to the tweets {tweets_for_topic}?"
                 f"please return just a number and nothing else",
        temperature=0.0).choices[0].message['content'])
    mongo_client.save_insights(topic, rate)
    return f"the satisfaction of the people about the tweets {tweets_for_topic} is {rate}"


@app.route('/visualize')
def visualize():
    """
    visualize the insights for the given topic
    the X axis is the tweet number and the Y axis is the insight satisfaction
    call /visualize?topic=topic_name
    if you want to see the graph in your machine, save the returned values as var named 'data' and run the following code:

    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.DataFrame(data)
    plt.plot(df['X'], df['Y'])
    plt.xlabel('tweet number')
    plt.ylabel('insight satisfaction')
    plt.title('tweet to satisfaction graph')
    plt.grid(True)
    plt.show()


    """
    topic = request.args.get('topic')
    insights = mongo_client.get_insights(topic)
    x_values = range(1, len(insights) + 1)  # Generate x values from 1 to length of the list
    plt.plot(x_values, insights, marker='o', linestyle='-')
    plt.xlabel('tweet number')
    plt.ylabel('insight satisfaction')
    plt.title('tweet to satisfaction graph')
    plt.grid(True)
    plt.xticks(np.arange(min(x_values), max(x_values) + 1, 1))
    plt.show()
    return {"x": x_values, "y": insights}
