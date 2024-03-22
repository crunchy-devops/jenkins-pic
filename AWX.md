# Install AWX 


## Latest version of AWX
```shell    
cd 
git clone -b 24.0.0 https://github.com/ansible/awx.git # check awx tag stable version
source jenkins-pic/venv/bin/activate
cd awx
make docker-compose-build
make docker-compose COMPOSE_UP_OPTS=-d
# use shell or portainer
docker exec -ti tools_awx_1 awx-manage createsuperuser
docker exec tools_awx_1 make clean-ui ui-devel
```


## Create a Team
![awx_team](screenshots/awx_team.png)

## Create a user 
![awx_user](screenshots/awx_user.png)

## Create a Credential for ssh 
![awx_ssh](screenshots/awx_credentials_machine.png)

## Create a Credential for gitlab
![awx_ssh](screenshots/awx_credentials_gitlab.png)

## Create a inventory source 
![awx_inventory](screenshots/awx_inventory_source.png)

## Create a projet
![awx_projet](screenshots/awx_projet.png)

## Create a template
![awx_template](screenshots/awx_template.png)

## Results





------------------------------------------------------------------
## Old install of AWX 17.1.0
```shell
cd    # set to your home directory 
git clone https://github.com/ansible/awx.git   # get the awx github repo 
cd awx   # current directory
git checkout 17.1.0  # latest version using docker
git branch  # Check if it is ok
python3 -m venv venv   # python virtualenv
source venv/bin/activate  # set the new environment 
pip3 install wheel   # permission
pip3 install requests  # internal 
pip3 install docker==6.1.3   # docker python lib
pip3 install docker-compose # docker script
pip3 install ansible  # provisioning tool
cd installer #  
# create a file vars.yml and copy and paste these 3 following lines
admin_password: 'adminpass'
pg_password: 'pgpass'
secret_key: 'mysupersecret'
# hit the command
ansible-playbook -i inventory install.yml -e @vars.yml

```