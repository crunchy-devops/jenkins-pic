FROM bitnami/jenkins

USER 0
RUN apt update && \
    apt -y install curl wget sudo nodejs npm && \
    apt -y install python3 python3-pip vim && \
    ln -s /jmeter/bin/jmeter /usr/bin/jmeter

