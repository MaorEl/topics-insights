from flask import Flask, request, render_template
from core_handler import *
app = Flask(__name__)


@app.errorhandler(ValueError)
def handle_value_error(e):
    return f'Error occurred: {str(e)}', 500


@app.route('/')
def docs():
    return render_template('docs.html')


@app.route('/signUp')
def sign_up():
    """
    sign up a new user with the given topics
    call /signUp?user_id=my_user_id&topics=topic1,topic2,topic3
    """
    args = request.args
    user_id = args['user_id']
    topics = args['topics']
    return core_sign_up(user_id, topics)


@app.route('/analyze')
def analyze():
    """
    analyize the given topic,
    call /analyze?topic=topic_name
    """
    topic = request.args['topic']
    return core_analyze(topic)


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
    return core_visualize(topic)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2345)
