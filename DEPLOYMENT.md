# Deployment using Docker 
Using Docker , the deployment stage is done by a Dockerfile inside the 
git repo itself. This is the part of Devops where the infrastructure is in a code. (IaC)

## Create a Docker build job
Create a job hello_world_docker_build  
Go to New Item -> Enter a name -> Freestyle -> ok    
Source code management  
Check git, provides the git repo of hello-world
Build  
Select Execute shell and copy/paste  
In the script, the Nexus war file is injected in a Docker image of Tomcat server
```shell script
 rm -Rf webapp.war
 wget http://<ip_address>:18081/repository/maven-releases/com/example/maven-project/maven-project/1.1/maven-project-1.1.war -O ${WORKSPACE}/webapp.war
 docker build -t hello-world-afip:latest .
```
Now we have a complete infrastructre for running ou code. 

## Run  Docker container as a testing environment 
Create a job hello_world_docker_test  
Go to New Item -> Enter a name -> Freestyle -> ok    
Source code management  
You don't need to tick git as the source is within the docker image
Build
Selecte Execute shell and copy/paste
```shell script
CONTAINER_NAME="hello-world-test"
OLD="$(docker ps --all --quiet --filter=name="$CONTAINER_NAME")"
if [ -n "$OLD" ]; then
  docker rm -f $OLD
fi
docker run -d --name hello-world-test -p 8090:8080 hello-world-afip
```
  
