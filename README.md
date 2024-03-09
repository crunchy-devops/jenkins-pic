# Jenkins CI-CD SandBox

(**Beware:** for a production usage you must set up this project on a Paas such as kubernetes or Openshift). 

This Github Repo contains all relevant files for setting up an entirely CI/CD sandbox.

![Docker CI Tools](screenshots/pic.png)

This sandbox is only available on Linux.

## Pre-requisite
You need a VM  ubuntu 20.04, 16GB of RAM, 4/6 cores, and 70 GB of SSD.

How to proceed ?  
## First install Docker 
sudo apt-get update  # update repo ref
sudo apt install -y python3.8-venv docker.io python3-pip  # install docker ce package
sudo usermod -aG docker $USER

### Install portainer 
```shell
docker volume create portainer_data
docker run -d -p 32125:8000 -p 32126:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock \
 -v portainer_data:/data portainer/portainer-ce:latest
# log on https://<ip>:32126
#set a password and activate portainer , you should see one container
```

### Install docker-compose 
```shell script
  cd jenkins-pic
  python3 -m venv venv
  source venv/bin/activate
  pip3 install docker==6.1.3
  pip3 install docker-compose # pip lib for docker-compose 
  docker-compose --version  # check should be version 1.29.2
```
I am using lts jenkins version, for persistence the jenkins home is mapped to a docker volume   
Edit and analyslle the docker-compose file and see the usage of volumes, services and network  

## Launch all containers
Hit the following commands for starting up all containers
```shell
docker-compose build # build all containers 
docker-compose up -d  # launch all containers
docker ps 
# Check, 8 jenkins-pic_xxx containers should be up and running
```

## Troubleshooting Sonarqube container
for sonarqube  
Add ```sudo sysctl -w vm.max_map_count=262144```   
or  
add this line   
```vm.max_map_count=262144```  
in /etc/sysctl.conf  
and run   
```sudo sysctl -p ```  
to reload configuration with new value


## Recreate the main user 
Go to jenkins  
Got to portainer and select jenkins-pic_jenkins_1  
edit /bitnami/jenkins/home/config.xml   
change the ```<useSecurity>true</useSecurity>```  
to  
```<useSecurity>false</useSecurity>```  
restart the container  
Open your Chrome Browser        
type the URL  http://<your_vm_ip_address>:32500      
Go to people, and delete the current people named user   
Go to security et select  
![Security](screenshots/security.png)  
Hit save and you got right away the user screen to fill in.  

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

## Go to FIRST_JOB.md file and follow the instructions

* IntellijIDEA.mnd
* DEPLOYMENT.md
* PIPELINE_SCRIPT.md
* AWX.md
* JMETER.md
* SELENIUM.md
* PIPELINE_GUI.md

Optional: DOCKER.md 

==== clean up ====
docker system prune --all --volumes
docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker volume rm $(docker volume ls -q)

=== remove docker =======
sudo systemctl stop docker
sudo apt-get purge docker-ce -y
sudo apt-get autoremove --purge docker-ce -y
sudo groupdel docker
sudo rm -rf /var/lib/docker
sudo rm -rf /etc/docker

=== dind === 
docker run -d --name test-dind --privileged -p 31999:2376 docker:dind