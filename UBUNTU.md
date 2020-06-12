# Install on Ubuntu

## Pre-requisites on your VM
### Usefull packages  
```shell script 
   sudo apt-get update  # update links to repos
   sudo apt-get -y install git wget htop iotop iftop # install git and monitoring tools
   sudo apt-get -y install python3 python3-venv # install python3 and virtualenv
``` 
### install this repo and docker    
```shell script
git clone   https://github.com/<your_personnal_repo>/jenkins-pic.git
cd jenkins-pic 
python3 -m venv venv  # set up the module venv in the directory venv
source venv/bin/activate  # activate the virtualenv python
pip3 install wheel  # set for permissions purpose
pip3 install ansible # install ansible 
ansible-playbook -i inventory install_docker_ubuntu.yml # run the playbook for installing docker
```