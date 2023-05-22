FROM ubuntu:20.04

RUN apt update && \
    apt -y install curl git &&  \
    curl -fsSL https://deb.nodesource.com/setup_18.x |  bash - && \
    apt -y install nodejs && \
    npm install -g @angular/cli

# RUN git clone https://github.com/crunchy-devops/angular-realworld-example-app.git
# WORKDIR /app
COPY . /app
RUN npm install --global yarn && \
    yarn install

EXPOSE 4200

CMD ["/usr/bin/ng", "serve", "--host", "0.0.0.0"]
