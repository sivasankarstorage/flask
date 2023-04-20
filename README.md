# README

This is the [Flask](http://flask.pocoo.org/) [quick start](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application) example for [Render](https://render.com).

The app in this repo is deployed at [https://flask.onrender.com](https://flask.onrender.com).

## Deployment

Follow the guide at https://render.com/docs/deploy-flask.

Build docker file :
docker build -t python-hello-world .

Run the container :
docker run -p 5000:5000 python-hello-world

Check the container is running in the background :
docker ps -a

stop the container
docker stop <container Id>

start the container in the background
docker start <container Id>

Go to the postman and hit the api
GET : http://localhost:5000/HelloGreeting?name=some

Remove container from the machine
docker rm <container Id1> <container Id2> <container Id3>
