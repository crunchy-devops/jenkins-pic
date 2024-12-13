# Jenkins with SSL key


```shell
openssl req -newkey rsa:2048 -nodes -keyout jenkins.key -x509 -days 365 -out jenkins.crt
openssl pkcs12 -export -out jenkins.p12 -inkey jenkins.key -in jenkins.crt -name jenkins
keytool -importkeystore -srckeystore jenkins.p12 -srcstoretype pkcs12 -destkeystore jenkins.jks -deststoretype JKS
sudo apt install openjdk-21-jre-headless
keytool -importkeystore -srckeystore jenkins.p12 -srcstoretype pkcs12 -destkeystore jenkins.jks -deststoretype JKS
```