## Topics Analyzer API
This is the API Gateway for the Topics Insights application. It is responsible to get REST request from users and represent our external layer which is open to get network traffic from the public internet.


## How to use?
1. Clone the repository
2. Run the following command to Build an image
```bash
docker build -t topics-api .
```
3. Run the following command to start the server
```bash
docker run -p 2345:2345 topics-api
```

## How to publish a new image?
1. Build image as before
```bash
docker build -t topics-api .
```
2. Tag the image:
```bash
docker tag topics-api maorel/topics-api:<version>
```

3. Push the image to the registry
```bash
 docker push maorel/topics-api:<version>
```


