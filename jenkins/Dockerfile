#FROM jenkins/jenkins:lts-jdk11
FROM bitnami/jenkins

USER 0
RUN apt update && \
    apt -y install curl wget && \
    #sudo apt install apt-transport-https ca-certificates curl software-properties-common
    apt -y install python3 python3-pip vim && \
    ln -s /jmeter/bin/jmeter /usr/bin/jmeter # && \
    chmod 777 /var/run/docker.sock \
    sed -i "/<useSecurity>true</useSecurity>/<useSecurity>false</useSecurity>/g" /bitnami/jenkins/home/config.xml
    #curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    #apt-get install -y nodejs && \
    #npm install -g @angular/cli



