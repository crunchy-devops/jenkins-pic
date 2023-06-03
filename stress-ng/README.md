# Stress-ng 

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
docker run -d --name web  -p 30452:5432 -e  POSTGRES_PASSWORD=password postgres
docker run -d -p 30460:9187 --name exporter1 \
-e DATA_SOURCE_NAME="postgresql://postgres:password@localhost:30452/postgres?sslmode=disable" \
quay.io/prometheuscommunity/postgres-exporter
```
