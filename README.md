# topics-insights

Application to get the most recent insights about your topics of interest.
This repository contains all the services to run the application.
cd to the right directory and run the following command to install the dependencies:

``` pip install -r requirements.txt```

## Topics Insights

### topics-analyzer-api
This microservice is responsible to get REST request from users and represent our external layer which is open to get network traffic from the public internet.

**It is allowing registration of new topics in the system and getting insights about them.**
**It is also responsible to get the request from the user and send it to the topics-analyzer service to get the insights about the topics of interest.**

### topics-core

This microservice is responsible for most of the business logic of the application. It is responsible to get the request from the topics-analyzer-api. It can get network traffic only from the topics-insight system and cannot be reached by the PUBLIC network.

### topics-ingestor

This microservice is responsible to get the data from the external sources and persist it in the database. It can get network traffic only from the topics-insight system and cannot be reached by the PUBLIC network.

### topics-twitter-gateway

This microservice is responsible to read tweets from the Twitter API and send it to the topics-ingestor to persist it in the database. It can get network traffic only from the topics-insight system and cannot be reached by the PUBLIC network.

### topics-db-client

This library is responsible to connect to the database and get the data from it or persist it in it. 
