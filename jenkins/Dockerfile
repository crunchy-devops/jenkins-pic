#FROM bitnami/jenkins
FROM bitnamilegacy/jenkins:2.516.2-debian-12-r0
RUN mkdir -p /bitnami/jenkins/home/checkimages/build
COPY check-docker-images.py /bitnami/jenkins/home/checkimages
COPY jenkins.jks /bitnami/jenkins/home/jenkins.jks
USER 0
RUN apt update && \
    apt -y install curl wget sudo && \
    apt -y install python3 python3-pip python3-pandas vim && \
    ln -s /jmeter/bin/jmeter /usr/bin/jmeter
    # acces to jenkins https
    #chown -R jenkins:jenkins /bitnami/jenkins/home/checkimages
RUN curl -L "https://github.com/docker/compose/releases/download/v2.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose && \
    chmod +x /usr/bin/docker-compose


