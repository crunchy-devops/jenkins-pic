# Docker overview
Install docker and hit the first command  
```shell script
     docker run docker/whalesay cowsay Hello-world!
```
Create a container and switch to background mode 
```shell script
   docker run -it --name mycontainer centos /bin/bash
   hostname
   exit
   docker start mycontainer
   docker attach mycontainer
   # Switch to background using Crtl-p Crtl-q
   docker ps
```
Start a container in background with -d flag 
```
  docker run -it -d --name mycontainer centos /bin/bash
```
Useful commands
```shell script
docker stop $(docker ps -aq)
# delete all containers
docker rm $(docker ps -aq)
# delete all images 
docker rmi  $(docker images -q)
````






