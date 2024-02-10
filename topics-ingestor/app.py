
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
scheduler.add_job(ingest_tweets, 'interval', minutes=1)
scheduler.start()


@app.route('/')
def hello_world():
    ingest_tweets()
    return 'I am topics ingestor and I will ingest more tweets for all of our customers every 5 minutes!'


if __name__ == '__main__':
    app.run(port=1234)
