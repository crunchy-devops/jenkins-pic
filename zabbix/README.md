# zabbix

## install zabbix server and agent 
```shell
wget https://repo.zabbix.com/zabbix/6.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.4-1+ubuntu20.04_all.deb
sudo dpkg -i zabbix-release_6.4-1+ubuntu20.04_all.deb
sudo apt update
sudo apt -y install zabbix-server-pgsql zabbix-frontend-php php7.4-pgsql zabbix-apache-conf zabbix-sql-scripts zabbix-agent
docker volume create postgresql-db
docker run -d --name db -v postgresql-db:/bitnami/postgresql -p 32432:5432 \ 
-e POSTGRESQL_PASSWORD=password bitnami/postgresql:13
```

## Use Portainer 
```shell
docker volume create portainer_data
docker run -d -p 32125:8000 -p 32126:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest 
```

## Reset Portainer password 
```shell
docker stop portainer
docker pull portainer/helper-reset-password
docker run --rm -v portainer_data:/data portainer/helper-reset-password
```

## install only a zabbix agent on a remote host
```shell
wget https://repo.zabbix.com/zabbix/6.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.4-1+ubuntu20.04_all.deb
sudo dpkg -i zabbix-release_6.4-1+ubuntu20.04_all.deb
sudo apt update
sudo apt -y install zabbix-agent
sudo vi /etc/zabbix/zabbix_agentd.conf
# add server ip address
sudo systemctl restart zabbix-agent
sudo systemctl enable zabbix-agent

```

![zabbix_host](../screenshots/zabbix_host.png)


