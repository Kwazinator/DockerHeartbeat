#!/bin/bash
sudo docker build -t potmheartbeat .
sudo docker run -d potmheartbeat
ECHO "type sudo docker ps to see running process"
ECHO "to stop type sudo docker stop <container id> container id can be found using sudo docker ps"


