# Dfinder-App

A FastApi/VueJS app for determining an easy and precise way for dividing a paper
into an odd number, for making a grid. Based on RJLang's ReferenceFinder.

I decided to put everything in a single container for increased ease of use.

# use
Currently, there is a docker container published!
If you want to run the app, simply fire up docker:
```
docker run --publish 1312:80 --name dfinder --detach --restart always ghcr.io/feefladder/dfinder-app:main
```
where:
 - `--publish` (`-p`) opens the port of the docker container. It maps 80->1312, so 1312 will be available
 - `--name` names the container, for easier reference.
 - `--detach` (`-d`) detaches the container, similar to `&`
 - `--restart always` makes sure the container always restarts. Handy in production. Also currently Dfinder uses static variables and crashes if concurrent calls are made. This is on the roadmap!

then open up a browser at `http://localhost:1312` and use the app!

## contributing/advanced use

clone the repo:
```
git clone git@github.com:feefladder/dfinder-app.git
cd dfinder-app
```
build the container:
```
docker build . --tag dfinder-latest
docker run --publish 1312:80 --name dfinder dfinder-latest
firefox http://localhost:1312/
```

### quick serve
This is useful so that you don't have to build a Docker container every time.
Make sure to change back when committing, or building a container:
#### Run the backend:
uncomment in dfinder-app/dfinder-app/main.py:
```
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
then run the uvicorn server on port 5000:
```
cd dfinder-app/dfinder-app/
poetry run uvicorn --port 5000 --root-path /api main:app
```

#### Run the frontend:
change the following lines:
```
const API_BASE = "http://127.0.0.1:5000/"
// const API_BASE = `${location.protocol}//${host}:${port}/api/`
```
then run the frontend application:
```
cd web-2
yarn serve
```
frontend will automatically update if you make changes.
## thanks
Special thanks go to:
 - Robert Lang for the algorithm
 - Docat for the Docker setup
 - Pybind11
