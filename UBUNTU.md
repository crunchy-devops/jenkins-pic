# Install on Ubuntu

## Pre-requisites on your VM
### Useful packages  
```shell
   sudo apt-get update  # update links to repos
   sudo apt-get -y install git wget htop iotop iftop # install git and monitoring tools
   sudo apt-get -y install python3 python3-venv # install python3 and virtualenv
   sudo apt-get -y install build-essential   # need for installing docker-compose
   sudo apt-get -y install python3-dev libxml2-dev libxslt-dev libffi-dev # need for installing docker-compose
   htop  # check your vm config
   Crtl-c  # exit 
``` 
### install this repo and docker    
```shell script
git clone   https://github.com/<your_personnal_repo>/jenkins-pic.git
cd jenkins-pic 
python3 -m venv venv  # set up the module venv in the directory venv
source venv/bin/activate  # activate the virtualenv python
pip3 install wheel  # set for permissions purpose
pip3 install ansible # install ansible 
pip3 install requests # extra packages
ansible --version # check the version number # should be the latest 2.10.8+ 
ansible-playbook -i inventory_for_ubuntu install_docker_ubuntu.yml # run the playbook for installing docker
```
Log out from your ssh session, close Jetbrains and log in again so all changes will take effect.  
Type ``` docker ps``` as ubuntu user for checking if all is fine.   
 
 