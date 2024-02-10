from flask import Flask
import logging
from tweeter_gateway import TweeterGateway

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# create an instance of the TweeterGateway and use it later on route
tweeter_gateway = TweeterGateway()


@app.route('/twitter-gateway/search/<topic>', methods=['GET'])
def search(topic):
    logging.info(f'Searching for tweets about: {topic}')
    search_results = tweeter_gateway.search(topic)
    return search_results


if __name__ == '__main__':
    app.run()
