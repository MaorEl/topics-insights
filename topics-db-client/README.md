how to install?
execute:
pip install git+https://github.com/MaorEl/topics-insights.git@add_setup#subdirectory=topics-db-client 

how to use?
from your .py file do:
from db import mongo_client
options -
mongo_client.sign_up
mongo_client.save_tweets
mongo_client.get_tweets