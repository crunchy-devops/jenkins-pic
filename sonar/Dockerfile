#
# Creates a docker container with SonarQube, incl. several plugins
#

FROM centos:7

MAINTAINER Herve Meftah<dockerlite@gmail.com>

#
# Set the JAVA_HOME variable to make it clear where Java is located
#ENV JAVA_HOME /usr/lib/jvm/java-1.8.0
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

RUN yum install -y openssl curl ca-certificates fontconfig gzip tar \
    && yum update -y; yum clean all

ENV JAVA_VERSION jdk-11.0.7+10
RUN set -eux; \
    ARCH="$(uname -m)"; \
    case "${ARCH}" in \
       aarch64|arm64) \
         ESUM='3b8b8bba6a0472ec7de5271cbf67f11e6ab525de6dd5d4729300375f1d56b7a1'; \
         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.7%2B10/OpenJDK11U-jdk_aarch64_linux_hotspot_11.0.7_10.tar.gz'; \
         ;; \
       armhf|armv7l) \
         ESUM='45c235af67498f87e3dc99642771e57547cf226335eaee8a55d195173e66a2e9'; \
         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.7%2B10/OpenJDK11U-jdk_arm_linux_hotspot_11.0.7_10.tar.gz'; \
         ;; \
       ppc64el|ppc64le) \
         ESUM='a417db0295b1f4b538ecbaf7c774f3a177fab9657a665940170936c0eca4e71a'; \
         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.7%2B10/OpenJDK11U-jdk_ppc64le_linux_hotspot_11.0.7_10.tar.gz'; \
         ;; \
       s390x) \
         ESUM='d9b72e87a1d3ebc0c9552f72ae5eb150fffc0298a7cb841f1ce7bfc70dcd1059'; \
         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.7%2B10/OpenJDK11U-jdk_s390x_linux_hotspot_11.0.7_10.tar.gz'; \
         ;; \
       amd64|x86_64) \
         ESUM='ee60304d782c9d5654bf1a6b3f38c683921c1711045e1db94525a51b7024a2ca'; \
         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.7%2B10/OpenJDK11U-jdk_x64_linux_hotspot_11.0.7_10.tar.gz'; \
         ;; \
       *) \
         echo "Unsupported arch: ${ARCH}"; \
         exit 1; \
         ;; \
    esac; \
    curl -LfsSo /tmp/openjdk.tar.gz ${BINARY_URL}; \
    echo "${ESUM} */tmp/openjdk.tar.gz" | sha256sum -c -; \
    mkdir -p /opt/java/openjdk; \
    cd /opt/java/openjdk; \
    tar -xf /tmp/openjdk.tar.gz --strip-components=1; \
    rm -rf /tmp/openjdk.tar.gz;

ENV JAVA_HOME=/opt/java/openjdk \
    PATH="/opt/java/openjdk/bin:$PATH"

ENV SONAR_VERSION 8.3.1.34397
ENV SONARQUBE_HOME /opt/sonarqube

# Plugin Versions
ENV SONAR_JAVA_PLUGIN 4.2
ENV SONAR_WEB_PLUGIN 2.4
ENV SONAR_SCM_GIT_PLUGIN 1.0


# Http port
EXPOSE 9000

# H2 Database port
EXPOSE 9092

# Install packages necessary
RUN yum -y install unzip && yum clean all

# Add SonarQube binaries from Nexus Repository
ADD https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-${SONAR_VERSION}.zip $SONARQUBE_HOME/sonarqube-${SONAR_VERSION}.zip

# Unpack SonarQube Zip
RUN set -x \
	&& unzip $SONARQUBE_HOME/sonarqube-${SONAR_VERSION}.zip \
	&& mv sonarqube-${SONAR_VERSION}/* $SONARQUBE_HOME \
	&& rm $SONARQUBE_HOME/sonarqube-${SONAR_VERSION}.zip

# Add plugins
#RUN mkdir -p $SONARQUBE_HOME/extensions/plugins/
#ADD http://central.maven.org/maven2/org/sonarsource/java/sonar-java-plugin/${SONAR_JAVA_PLUGIN}/sonar-java-plugin-${SONAR_JAVA_PLUGIN}.jar $SONARQUBE_HOME/extensions/plugins/sonar-java-plugin-${SONAR_JAVA_PLUGIN}.jar
#ADD http://central.maven.org/maven2/org/sonarsource/sonar-web-plugin/sonar-web-plugin/${SONAR_WEB_PLUGIN}/sonar-web-plugin-${SONAR_WEB_PLUGIN}.jar $SONARQUBE_HOME/extensions/plugins/sonar-web-plugin-${SONAR_WEB_PLUGIN}.jar
#ADD http://central.maven.org/maven2/org/codehaus/sonar-plugins/sonar-scm-git-plugin/${SONAR_SCM_GIT_PLUGIN}/sonar-scm-git-plugin-${SONAR_SCM_GIT_PLUGIN}.jar $SONARQUBE_HOME/extensions/plugins/sonar-scm-git-plugin-${SONAR_SCM_GIT_PLUGIN}.jar

COPY run.sh $SONARQUBE_HOME

WORKDIR $SONARQUBE_HOME

VOLUME ["$SONARQUBE_HOME/data","$SONARQUBE_HOME/conf","$SONARQUBE_HOME/logs"]

RUN chmod -R 777 $SONARQUBE_HOME

CMD ["/opt/sonarqube/run.sh"]
