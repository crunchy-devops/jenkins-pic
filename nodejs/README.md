# nodejs

## install
```shell
cd nodejs/
docker build -t nodejs-ubuntu .
docker run -it --name web nodejs-ubuntu /bin/bash
```
## in dockerfile
```shell
npm install -g @angular/cli
npm install --global yarn
yarn install
```

npm install --save-dev tslint-angular
apt install -y vim
vim package.json
“extends”: [“tslint:recommended”, “tslint-angular”],
ng lint --quiet