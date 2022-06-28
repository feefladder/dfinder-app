# Dfinder-App

A FastApi/VueJS app for determining an easy and precise way for dividing a paper
into an odd number, for making a grid. Based on RJLang's ReferenceFinder.

## installation (dev)
You need Docker
```
docker run --publish 1312:80 --name dfinder ghcr.io/feefladder/dfinder-app:main
```

```
git clone git@github.com:feefladder/dfinder-app.git
cd dfinder-app
docker build . --tag dfinder-latest
docker run --publish 1312:80 --name dfinder dfinder-latest
firefox http://localhost:1312/
```
## thanks
Special thanks go to:
 - Robert Lang for the algorithm
 - Docat for the Docker setup
 - Pybind11