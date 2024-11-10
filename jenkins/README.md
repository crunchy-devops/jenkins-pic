# Example 


docker images --all --filter=reference='robotshop/*:ebde46fae5ae' --format "table {{.Repository}}\t{{.Size}}" >/bitnami/jenkins/home/checkimages/build-11