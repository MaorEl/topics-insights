
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from ingestor import DataIngestor
from analyzer import DataAnalyzer
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
data_ingestor = DataIngestor()
data_analyzer = DataAnalyzer()


def ingest_tweets():
    data_ingestor.ingest_tweets()


def analyze_tweets():
    data_analyzer.analyze_topics()


scheduler = BackgroundScheduler()
scheduler.add_job(ingest_tweets, 'interval', seconds=300)
scheduler.add_job(analyze_tweets, 'interval', seconds=600)

scheduler.start()


@app.errorhandler(ValueError)
def handle_value_error(e):
    return f'Error occurred: {str(e)}', 500


@app.route('/')
def hello_world():
    return ('I am topics ingestor and I will ingest more tweets for all of our customers every 5 minutes!'
            ' I will also create insights for them every hour!')


if __name__ == '__main__':
    app.run(port=1234)
