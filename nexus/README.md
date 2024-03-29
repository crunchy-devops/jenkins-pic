## Nexus Docker Container

The Dockerfile builds and starts a Nexus repository and configures the JBoss Enterprise maven repos on Nexus.

### Usage - Pull Image from Docker Hub

```
docker pull ambient-docker/nexus
docker run -d -p 8081:8081 nexus
```

### Usage - Build manually

```
docker build -t nexus .
docker run -d -p 8081:8081 nexus
```
### Configure Nexus Docker registry
Create a docker registry hosted   
Set HTTP port to 20000  
Check Allow anomymous docker pull   
Deployment policy  to Allow redeploy
Go to Security -> Realms
Set active  Docker Bearer Token Realm

### Change docker daemon config

Add the following lines in /etc/docker/daemon.json

```json
{
  
        "insecure-registries":["nexus:20000"]
}
{
        "dns": ["8.8.8.8", "8.8.4.4"]
}
```

Add nexus entry in /etc/hosts as the example below

```shell
127.0.0.1 localhost
51.68.28.209 jenkins jenkins external.local
172.16.0.11 internal.local
172.18.0.2 nexus
```

### In jenkins 
how to registry an image  
Create a job with a build  

```shell
docker login -u $USER -p $PASSWORD http://nexus:20000
docker tag systemdevformations/alpine-ssh:v2 nexus:20000/alpine-ssh:v2
docker push nexus:20000/alpine-ssh:v2
```



