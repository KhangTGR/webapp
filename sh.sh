#!/bin/bash
if [[ $1 == 'up' ]]
then
    docker build -t webapp-image .
    docker run -e FLASK_DEBUG="True" -p 8080:8080 --name webapp-container -d webapp-image
elif [[ $1 == 'run' ]]
then
    docker rm -f webapp-container
    docker run -e FLASK_DEBUG="True" -p 8080:8080 --name webapp-container -d webapp-image 
elif [[ $1 == 'clean' ]]
then
    docker rm -f webapp-container
    docker rmi webapp-image
elif [[ $1 == 'start' ]]
then
    docker start webapp-container
elif [[ $1 == 'stop' ]]
then
    docker stop webapp-container
elif [[ $1 == 'ps' ]]
then
    docker ps -a
    docker images
else
    echo "Please enter either: up, clean, stop, ps"
fi
