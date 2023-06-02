# Scrape

## Basic commands
go to alert  
there are applicable to both endpoints  
enter go_threads  
enter process_virtual_memory_bytes  
zoom out  
more specific tsdb = time serie database  
select prometheus_tsdb_storage_blocks_bytes  
select node_load1  
select node_netstat_Tcp_InSegs  

## For example add a postgresql node-exporter
```shell
docker run -d --net=host -it --rm -e POSTGRES_PASSWORD=password postgres
# Connect to it
docker run -d \
  --net=host \
  -e DATA_SOURCE_NAME="postgresql://postgres:password@localhost:5432/postgres?sslmode=disable" \
  quay.io/prometheuscommunity/postgres-exporter
```







## Check syntax of yaml file 
```shell
docker exec -it lab-nginx-reverse-proxy_prometheus_1 promtool check config /etc/prometheus/prometheus.yml
```
## PromQL
function instance vector 
select ```scrape_duration_seconds{ instance="localhost:9100"}[1m]```  
check value in table  
https://www.epochconverter.com/  