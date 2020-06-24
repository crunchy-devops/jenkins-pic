# Deployment using Docker 
Using Docker , the deployment stage is done by a Dockerfile inside the  
git repo itself. This is the part of Devops where the infrastructure is in a code.(IaC)  

## Create a Docker build job
Create a job hello_world_docker_build  
Go to New Item -> Enter a name -> Freestyle -> ok      
Source code management  
Check git, provides the git repo of hello-world  
Build  
Select Execute shell and copy/paste the following script   
In the script, the Nexus war file is injected in a Docker image of Tomcat server  
```shell script
 rm -Rf webapp.war
 wget http://nexus:8081/repository/maven-releases/com/example/maven-project/maven-project/1.1/maven-project-1.1.war -O ${WORKSPACE}/webapp.war
 docker build -t hello-world-afip:latest .
```
Build
And apply and save
Now we have a complete infrastructure for running our code.
## Run  Docker container as a testing environment 
Create a job hello_world_docker_test  
Go to New Item -> Enter a name -> Freestyle -> ok    
Source code management  
You don't need to tick git as the source code is in the docker image  
Build  
Select Execute shell and copy/paste the following code  
```shell script
CONTAINER_NAME="hello-world-test"
OLD="$(docker ps --all --quiet --filter=name="$CONTAINER_NAME")"
if [ -n "$OLD" ]; then
  docker rm -f $OLD
fi
docker run -d --name hello-world-test -p 8090:8080 hello-world-afip
```
Hit a new tab in your browser and check   
```http://<ip_address_your_vm>:8090/webapp/```


