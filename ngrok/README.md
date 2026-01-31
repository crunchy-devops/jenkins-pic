# ngrok
ngrok est une passerelle complète et prête à l'emploi pour gérer le trafic public ou 
privé de vos applications et services, quel que soit leur emplacement d'exécution. 
En quelques étapes, vous pouvez utiliser ngrok comme proxy inverse de niveau entreprise, répartiteur de charge, 
passerelle API, pare-feu, réseau de diffusion de contenu (CDN), et bien plus encore.

## install ngrok
```shell
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
sudo tar -xvzf ~/Downloads/ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
# get a token 
ngrok config add-authtoken xxxxx
# open a tunnel to jenkins  in dedicated shell session
ngrok http 32500  # port de jenkins
```
