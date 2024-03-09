# Jenkins CI-CD SandBox

(**Beware:** for a production usage you must set up this project on a Paas such as kubernetes or Openshift). 

This Github Repo contains all relevant files for setting up an entirely CI/CD sandbox.

![Docker CI Tools](screenshots/pic.png)

This sandbox is only available on Linux.

## Pre-requisite
You need a VM  ubuntu 22.04, 16GB of RAM, 2/4 cores, and 40 GB of SSD.

How to proceed ?  
## First install Docker 
Go to **UBUNTU.md** markdown file and follow the instructions.

### Install portainer for managing containers
```shell
docker volume create portainer_data
docker run -d -p 32125:8000 -p 32126:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock \
 -v portainer_data:/data portainer/portainer-ce:latest
``` 
Rapidly (there is a timeout), log on **https://<ip_address>:32126**    
Set a password and activate portainer , you should see one container

### Install docker-compose 
```shell script
  cd jenkins-pic
  pip install pyyaml==5.3.1
  pip3 install docker==6.1.3
  pip3 install docker-compose # pip lib for docker-compose 
  docker-compose --version  # check should be version 1.29.2
```
I am using bitnami/version, for persistence the jenkins home is mapped to a docker volume  
Edit and analyse the docker-compose file and see the usage of volumes, services and network. 

## Launch all containers
Hit the following commands for starting up all containers
```shell
docker-compose build # build all containers 
docker-compose up -d  # launch all containers
docker ps 
# Check, 8 jenkins-pic_xxx containers should be up and running
```

## Sanity Test of Jenkins container 
Go to portainer  
Select the container jenkins-pic_jenkins_1  
Open a console on it   
type ```docker ps``` , you should see all running containers on your vm   
type ```jmeter --version``` , you should see jmeter prompt

## Troubleshooting Sonarqube container
On the vm for fixing the sonarqube container  
Add ```sudo sysctl -w vm.max_map_count=262144```   
or  
add this line   
```vm.max_map_count=262144```  
in /etc/sysctl.conf  
and run   
```sudo sysctl -p ```  
to reload configuration with this new value
go to portainer and restart the container jenkins-pic_sonar_1


## As bitnami jenkins is secure you must recreate the admin user 
Go to jenkins  
Got to portainer and select jenkins-pic_jenkins_1  
edit /bitnami/jenkins/home/config.xml   
change the ```<useSecurity>true</useSecurity>```  
to  
```<useSecurity>false</useSecurity>```  
restart the container jenkins-pic_jenkins_1
Open your Chrome Browser        
type the URL  http://<your_vm_ip_address>:32500      
Go to people, and delete the current people named user   
Go to Manage Jenkins, choose Security , see the image below  

![Security](screenshots/security.png)  

Hit save and you go right away the user screen to fill in.  

## Get an API token and set timezone
click on user in right hand side on a top of a screen  
Hit configure  
select API Token , Add new token , give jetbrains name  
and Hit generate 
copy this token in your notepad for later use.  
go to Defined time zone. Select Europe/Paris
Press apply and save   

## Overview
Here is an overview of all tools:
- Github is the well-known website for archiving all your projects.
- Jenkins contains build job and is triggered once projects in GitHub are updated.
- As part of the CI build, Jenkins triggers a static code analysis and the results are stored in SonarQube.
- The Maven build uses Nexus as a Proxy Repository for all 3rd party libs. The build artifacts are deployed to the Nexus Release Repository.
- Jmeter contains all requirements for running load testing and check performance regression.
- The Selenium Grid contains Docker containers running Chrome and Firefox and is used for UI tests.

## Access Tools
### With docker containers
| *Tool* | *Link*                                    | *Credentials* |
| --------- |-------------------------------------------| ------------- |
| Jenkins | http://<vm_ip default>:32500/             | to be defined |
| SonarQube | http://<vm_ip default>:32520/             | admin/admin |
| Nexus | http://<vm_ip default>:32510/nexus        | admin/use a token and set your own password |
| Selenium Grid | http://<vm_ip default>:30044/grid/console | no login required |
 | Jmeter | no required                               | no login required |
 | Portainer | **https**://<vm_ip default>:32126         | enter a password at first log in |
| Petclinic | http://<vm_ip default>:30190/petclinic    | no login required |

## See more MarkDown files with instructions

* FIRST_JOB.md 
* DEPLOYMENT.md
* JETBRAINS.md
* AWX.md
* JMETER.md
* SELENIUM.md
* AWX.md
* NEXUS_DOCKER_REGISTRY.md
* PIPELINE_GUI.md
* PIPELINE_SCRIPT.md

## Caveats ( some maintenance commands)
==== clean up all ====  
```
docker system prune --all --volumes
docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker volume rm $(docker volume ls -q)

=== remove docker daemon =======
sudo systemctl stop docker
sudo apt-get purge docker-ce -y
sudo apt-get autoremove --purge docker-ce -y
sudo groupdel docker
sudo rm -rf /var/lib/docker
sudo rm -rf /etc/docker

===  example of Docker dind === 
docker run -d --name test-dind --privileged -p 31999:2376 docker:dind
```