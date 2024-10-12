FROM bitnami/jenkins

USER 0
RUN apt update && \
    apt -y install curl wget sudo && \
    apt -y install python3 python3-pip vim && \
    ln -s /jmeter/bin/jmeter /usr/bin/jmeter
RUN curl -L "https://github.com/docker/compose/releases/download/v2.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose && \
    chmod +x /usr/bin/docker-compose

