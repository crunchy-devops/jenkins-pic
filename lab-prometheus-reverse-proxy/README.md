# Lab-prometheus-reverse-proxy
## Launch 2 containers prometheus and node-exporter 

```shell
# start prometheus and node-exporter
cd lab-prometheus-reverse-proxy
docker-compose up -d
```
## install nginx as reverse-proxy
```shell
sudo apt update
#sudo apt -y upgrade
sudo apt -y install nginx vim 
cd /etc/nginx/sites-enabled
sudo vim prometheus 
```
Copy and paste 
```shell
server {
    listen 80;
    listen [::]:80;
    server_name crunchydevops.com;
    
    location / {
         proxy_pass      http://localhost:9090/;
  
}
cd - 
sudo nginx -t 
sudo systemctl restart nginx

# Check 
http://domain.name     # so now you don't need to specify a port number
```
## Certbot
```shell
sudo snap install core 
sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx
# your prometheus file has changed
```
sudo systemctl restart nginx

## Basic authentication 
```shell
sudo apt -y install apache2-utils
# create htpassword
sudo htpasswd -c /etc/nginx/.htpasswd admin
sudo cd /etc/nginx/sites-enabled
sudo vim prometheus
```
### add lines
```shell
# addition authentication properties
auth_basic "Protected Area";
auth_basic_user_file /etc/nginx/.htpasswd;
```
sudo nginx -t 
sudo systemctl restart nginx

## iptables rules
```shell
#iptables -A INPUT -p tcp -s localhost --dport 9090 -j ACCEPT
#iptables -A INPUT -p tcp --dport 9090 -j DROP
#iptables -L
```
sudo firewall-cmd --zone=public --add-service=https
sudo firewall-cmd --zone=public --add-port=9090/tcp









