# Jenkins CI-CD SandBox

(**Beware:** for a production usage you must set up this project on a Paas such as kubernetes or Openshift). 

This Github Repo contains all relevant files for setting up an entirely CI/CD sandbox.

![Docker CI Tools](screenshots/pic.png)

This sandbox is only available on Linux.

## Pre-requisite
You need a VM  ubuntu 20.04, 16GB of RAM, 6 cores, and 60 GB of SSD.

How to proceed ?  
## First install Docker 
Go to the file UBUNTU.md 

### Install portainer 
```shell
docker volume create portainer_data
docker run -d -p 32125:8000 -p 32126:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock \
 -v portainer_data:/data portainer/portainer-ce:latest
# log on https://<ip>:32126
#set a password and activate portainer , ypu should see one container
```


### Install docker-compose 
```shell script
  cd jenkins-pic
  source venv/bin/activate
  pip3 install docker-compose # pip lib for docker-compose
  pip3 install docker # pip lib for docker 
  docker-compose --version  # check should be version 1.29.+
```
I am using lts jenkins version, for persistence the jenkins home is mapped to a docker volume   
Edit and analyse the docker-compose file and see the usage of volumes, services and network  

## Launch all containers
Hit the following commands for starting up all containers
```shell
docker-compose build # build all containers 
docker-compose up -d  # launch all containers
docker ps # Check, 7 jenkins-pic_xxx containers should be up and running
```

## Go to jenkins
Open your Chrome Browser      
type the URL  http://<your_vm_ip_address>:32500    
user name is : user   
password is : password  

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
- GitLab (optional) is used for storing the Source Code.
- Github is the well-known website for archiving all your projects.
- Jenkins contains build job and is triggered once projects in GitHub are updated.
- As part of the CI build, Jenkins triggers a static code analysis and the results are stored in SonarQube.
- The Maven build uses Nexus as a Proxy Repository for all 3rd party libs. The build artifacts are deployed to the Nexus Release Repository.
- Jmeter contains all requirements for running load testing and check performance regression.
- The Selenium Grid contains Docker containers running Chrome and Firefox and is used for UI tests.

## Access Tools
### With docker containers
| *Tool* | *Link*                                    | *Credentials* |
| ------------- |-------------------------------------------| ------------- |
| Jenkins | http://<vm_ip default>:32500/             | to be defined |
| SonarQube | http://<vm_ip default>:32520/             | admin/admin |
| Nexus | http://<vm_ip default>:32510/nexus        | admin/use a token and set your own password |
| Selenium Grid | http://<vm_ip default>:30044/grid/console | no login required |
 | Jmeter | no required | no login required |
| Hello-world Test | http://<vm_ip default>:30090/webapp       | no login required |
| Petclinic-Test | http://<vm_ip default>:30190/petclinic    | no login required |



* FIRST_JOBS.md
* IntellijIDEA.mnd
* DEPLOYMENT.md
* PIPELINE_SCRIPT.md
* AWX.md
* JMETER.md
* SELENIUM.md
* PIPELINE_GUI.md

Optional: DOCKER.md 