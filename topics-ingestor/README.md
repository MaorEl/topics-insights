## Topics Ingestor
This application is responsible for ingesting tweets about signed up topics from the Twitter API and storing them in a database.

## How to use?
1. Clone the repository
2. Run the following command to Build an image
```bash
docker build -t topics-ingestor .
```
3. Run the following command to start the server
```bash
docker run -p 1234:1234 topics-ingestor
```

## How to publish a new image?
1. Build image as before
```bash
docker build -t topics-ingestor .
```
2. Tag the image:
```bash
docker tag topics-ingestor maorel/topics-ingestor:<version>
```

3. Push the image to the registry
```bash
 docker push maorel/topics-ingestor:<version>
```


