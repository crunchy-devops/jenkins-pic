# Install on Ubuntu

## install Docker on ubuntu 24.04
```shell
sudo apt update
sudo apt install -y curl apt-transport-https ca-certificates software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce -y
sudo systemctl status docker
sudo usermod -aG docker $USER
# log out log in again
docker ps # check
```

## install docker-compose
```shell
sudo curl -L "https://github.com/docker/compose/releases/download/v2.30.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose
sudo chmod +x /usr/bin/docker-compose 
docker-compose version 
```

## install docker + docker-compose with python venv and Ansible
```shell
sudo apt update
sudo apt -y install python3-venv
cd jenkins-pic/
python3 -m venv venv
source venv/bin/activate
pip3 install wheel
pip3 install ansible
pip3 install setuptools
ansible-playbook -i inventory install_docker_ubuntu.yml --limit local
sudo curl -L "https://github.com/docker/compose/releases/download/v2.32.4/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
#pip3 install "cython<3.0.0" wheel && pip3 install pyyaml==5.4.1 --no-build-isolation
#pip3 install docker-compose
```
