FROM jenkins/jenkins:lts-jdk11

USER root
RUN apt-get update && \
    #apt-get upgrade && \
    apt-get -y install libmariadb-dev wget && \
    apt-get install -y python3 python3-pip && \
    ln -s /jmeter/bin/jmeter /usr/bin/jmeter
#RUN wget https://download.java.net/openjdk/jdk11/ri/openjdk-11+28_linux-x64_bin.tar.gz && \
#    mv openjdk-11+28_linux-x64_bin.tar.gz /opt && \
#    cd /opt && tar -zxvf openjdk-11+28_linux-x64_bin.tar.gz && \
#    rm openjdk-11+28_linux-x64_bin.tar.gz


