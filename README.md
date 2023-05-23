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


 
 * FIRST_JOBS.md
 * IntellijIDEA.mnd
 * DEPLOYMENT.md
 * PIPELINE_SCRIPT.md
 * AWX.md  
 * JMETER.md  
 * SELENIUM.md  
 * PIPELINE_GUI.md  
   
Optional: DOCKER.md 

## Pre-requis pour Centos 7
```
sudo yum -y update   # update all packages 
sudo yum -y install git wget   # install git and wget 
sudo yum -y install epel-release  # added extra packages
sudo yum -y install htop iotop iftop  # added monitoring tools
//Fork  
//     https://github.com/crunchy-devops/jenkins-pic.git
and git clone your personnal repository of jenkins-pic
git clone https://github.com/<your-repo>/jenkins-pic.git
cd jenkins-pic  
```
**Attention A NE PAS FAIRE les commandes suivantes, CHOISIR UNE INSTALLATION PAR ANSIBLE**
### Installation de la derniere version de Docker sous Centos 
L'installation de Docker necessite certains packages.
```
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```
Ensuite nous devons mettre en place le lien vers le repository Docker.
```
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```
Installer la derniere version de Docker et de ses packages client et containerd.io
```
 sudo yum install docker-ce docker-ce-cli containerd.io
```
Lancer le daemon Docker 
```
sudo systemctl start docker
```
Placer un lien symbolique pour que le daemon Docker demarre automatiquement meme si le host est reboote. 
```
sudo systemctl enable docker
```

## Ou par une installation de Docker avec un script Ansible 
### Packages de pre-requis pour installer Ansible 
```
sudo yum -y install python3 
```

### Set up a python virtualenv, and install ansible
```shell script
  # in the jenkins-pic directory 
  cd jenkins-pic
  python3 -m venv venv  # install virtualenv module dans la directory venv
  source venv/bin/activate # activate the python virtualenv
  pip3 install wheel  # install pip package wheel for permission usage
  pip3 install --upgrade pip
  pip3 install ansible # install ansible
  ansible --version  # check, should be version 2.10.5
```

### Lancement de la commande ansible-playbook qui va installer Docker
```
  ansible-playbook -i inventory  playbook.yml
```

Please log out and log in again of your shell screen for 
the changes take effect. 
```shell script
   docker ps    # check if docker is up and running 
```

### Run portainer 
```shell
docker run -d -p 9000:9000 --name portainer -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer -H unix:///var/run/docker.sock 
```


### Install docker-compose 
```shell script
  cd jenkins-pic
  source venv/bin/activate
  pip3 install docker-compose # pip lib for docker-compose
  pip3 install docker # pip lib for docker 
  docker-compose --version  # check should be version 1.29.+
```
Using the lts jenkins version, the jenkins home is a docker volume   
See in the docker-compose file jenkins volume and services  

## Launch all containers
Hit the command for starting up all containers
```shell
docker-compose build # build all containers 
docker-compose up -d  # launch all containers
docker ps # Check, 7 jenkins-pic_xxx containers should be up and running
```

## Go to jenkins
Open your Chrome Browser    
type the URL  http://<your_vm_ip_address>:32500   

## Get the secret key 
type ``` docker logs jenkins-pic_jenkins_1 ```  
scroll the log file, and get the secret value  
**DO NOT install any plugins now, we need a fresh install** 

## Change admin password, get an API token, set timezone
click on admin in right hand side of a screen  
Hit configure  
select API Token , Add new token , give jetbrains name  
and Hit generate 
copy this token in your notepad for later use. 
change the password and confirm  
go to Defined time zone. Select Europe/Paris
Press apply and save  
You may get some errors so you need to login in again using your new password. 

## Overview
Here is an overview of all tools:
- GitLab (optional) is used for storing the Source Code.
- Github is the well-known website for archiving all your projects.
- Jenkins contains build job and is triggered once projects in GitLab are updated.
- As part of the CI build, Jenkins triggers a static code analysis and the results are stored in SonarQube.
- The Maven build uses Nexus as a Proxy Repository for all 3rd party libs. The build artifacts are deployed to the Nexus Release Repository.
- The Selenium Grid contains Docker containers running Chrome and Firefox and is used for UI tests.

## Access Tools
### With docker containers
| *Tool* | *Link*                                    | *Credentials* |
| ------------- |-------------------------------------------| ------------- |
| Jenkins | http://<vm_ip default>:32500/             | to be defined |
| SonarQube | http://<vm_ip default>:32520/             | admin/admin |
| Nexus | http://<vm_ip default>:32510/nexus        | admin/use a token and set your own password |
| Selenium Grid | http://<vm_ip default>:30044/grid/console | no login required |
| Hello-world Test | http://<vm_ip default>:30090/webapp       | no login required |
| Petclinic-Test | http://<vm_ip default>:30190/petclinic    | no login required |
| AWX-ansible| http://<vm_ip default>                    | admin/password |
