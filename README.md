# Debugging a Python Flask app in Docker Compose

This is the companion repository to [this blog post (Medium)](https://medium.com/@trstringer/debugging-a-python-flask-application-in-a-container-with-docker-compose-fa5be981ec9a)

## Running the application

```
$ docker-compose run --build -d
```

## Debugging the application

If changes were made to the file (e.g. added breakpoint), build first...

```
$ docker-compose build
```

Run the application in Docker Compose but specify a particular command...

```
$ docker-compose run -p 8000:8000 svc1 python3 -m pdb app.py
```

Debug the application as you would any other Python application

## Interacting with the application

### Display simple message

```
$ curl localhost:8000
```

### Add message to application (Redis cache)

```
$ curl -X POST localhost:8000/message/<message_to_add>
```

### Get message from application (stored in Redis)

```
$ curl -X POST localhost:8000/message
```
