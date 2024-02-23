## Topics Core
This is the core of the topics application. It is responsible for the business logic of the application.

## How to use?
1. Clone the repository
2. Run the following command to Build an image
```bash
docker build -t topics-core .
```
3. Run the following command to start the server
```bash
docker run -p 8080:8080 topics-core
```

## How to publish a new image?
1. Build image as before
```bash
docker build -t topics-core .
```
2. Tag the image:
```bash
docker tag topics-core maorel/topics-core:<version>
```

3. Push the image to the registry
```bash
 docker push maorel/topics-core:<version>
```


