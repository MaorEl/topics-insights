
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from ingestor import DataIngestor
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
data_ingestor = DataIngestor()


def ingest_tweets():
    data_ingestor.ingest_tweets()


scheduler = BackgroundScheduler()
scheduler.add_job(ingest_tweets, 'interval', seconds=300)
scheduler.start()


@app.errorhandler(ValueError)
def handle_value_error(e):
    return f'Error occurred: {str(e)}', 500


@app.route('/')
def hello_world():
    return 'I am topics ingestor and I will ingest more tweets for all of our customers every 5 minutes!'


if __name__ == '__main__':
    app.run(port=1234)
