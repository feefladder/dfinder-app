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
## thanks
Special thanks go to:
 - Robert Lang for the algorithm
 - Docat for the Docker setup
 - Pybind11
