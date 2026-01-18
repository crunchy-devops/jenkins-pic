# ALMA

## install docker on almalinux 10.1
```shell
sudo dnf -y --refresh update
sudo dnf upgrade
sudo dnf -y install yum-utils git wget curl
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl status docker
docker --version
id
sudo usermod -aG docker $USER
# restart pycharm 
id 
docker ps
```

## docker compose
```shell
sudo curl -L "https://github.com/docker/compose/releases/download/v5.0.1/docker-compose-linux-x86_64"  -o  /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

### Install portainer for managing containers
```shell
docker volume create portainer_data
docker run -d -p 32125:8000 -p 32126:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock \
 -v portainer_data:/data portainer/portainer-ce:2.20.2-alpine
```
There is a timeout login so log in  immediately

