# Desafio Fundação CERTI
API source code - Numbers into Words Converter, numbers in the range of - 99999 and 99999. 

The application developed in [Flask](https://flask.palletsprojects.com/en/1.1.x/), [Python](https://docs.python.org/3/) and a [WSGI](https://www.fullstackpython.com/wsgi-servers.html) server to listen to requests.

## Requirements

Only Docker to Build image and run application:

- [Docker](https://docs.docker.com/docker-for-windows/install/)


##Getting started

To run the application, in the directory where the DockerFile file is located, open the Power Shell and type the commands:

- Build Image:
docker build -t image_name PATH
  
Example:
```
docker build -t certi .

```

- Run Image:
```
docker run -p 3000:3000 certi
```
After the RUN command, the WSGI server will be running on the local machine listening for HTTP requests on port 3000.



##Testing the application
Open your browser and access the address:

- Home: http://localhost:3000/
- Numbers into Words Converter, for exemplo: http://localhost:3000/12345

results:
```json
{"extenso":"doze mil e trezentos e quarenta e cinco"}
```