# Example 
See the Python script check-docker-images.py
This script monitors the size of your app project's Docker images and ensures that they don't increase by more than 25% between Jenkins builds. Stay ahead of potential issues and maintain optimal performance!


## some example for testing the script
```shell
docker images --all --filter=reference='robotshop/*:ebde46fae5ae' --format "table {{.Repository}}\t{{.Size}}" >/bitnami/jenkins/home/checkimages/build-11
```