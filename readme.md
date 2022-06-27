# Dfinder-App

A FastApi/VueJS app for determining an easy and precise way for dividing a paper
into an odd number, for making a grid. Based on RJLang's ReferenceFinder.

## installation
```
git clone git@github.com:feefladder/dfinder-app.git
cd dfinder-app
docker build . --tag dfinder-latest
docker run --publish 1312:80 --name dfinder dfinder-latest
firefox http://localhost:1312/
```