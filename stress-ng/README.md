# Stress-ng 

## Use Portainer
```shell
docker volume create portainer_data
docker run -d -p 32125:8000 -p 32126:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest 


## node-exporter 
```shell
docker run -d --name node-exporter -p 30100:9100 bitnami/node-exporter
```


## Install
```shell
docker run --rm ghcr.io/colinianking/stress-ng --help
```
## CPU stress
```shell
docker run --rm ghcr.io/colinianking/stress-ng --cpu 2 --vm 2 --hdd 1 --fork 8 --timeout 2m --metrics
```

## Stress Postgresql
```shell
docker run -d --name db3  -p 30452:5432 -e  POSTGRES_PASSWORD=password postgres
docker run -d -p 30460:9187 --name exporter1 \
-e DATA_SOURCE_NAME="postgresql://postgres:password@localhost:30452/postgres?sslmode=disable" \
quay.io/prometheuscommunity/postgres-exporter
```
## Load values
docker exec -it --user postgres db1 /bin/bash
drop table t_random;
create table t_random as select s, md5(random()::text) from generate_Series(1,500000000) s;
