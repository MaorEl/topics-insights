## Topics Twitter Gateway
This is a simple Twitter Gateway that allows you to get tweets from the twitter API

## How to use?
1. Clone the repository
2. Run the following command to Build an image
```bash
docker build -t topics-twitter-gateway .
```
3. Run the following command to start the server
```bash
docker run -p 5000:5000 topics-twitter-gateway
```

## How to publish a new image?
1. Build image as before
```bash
docker build -t topics-twitter-gateway .
```
2. Tag the image:
```bash
docker tag topics-twitter-gateway maorel/topics-twitter-gateway:<version>
```

3. Push the image to the registry
```bash
 docker push maorel/topics-twitter-gateway:<version>
```


