#FROM jenkins/jenkins:lts-jdk11
FROM bitnami/jenkins

USER root
RUN apt-get update && \
    apt-get -y install libmariadb-dev wget && \
    apt-get install -y python3 python3-pip && \
    ln -s /jmeter/bin/jmeter /usr/bin/jmeter  && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g @angular/cli



