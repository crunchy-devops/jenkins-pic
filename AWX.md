# AWX 17.1.0
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
pip3 install docker   # docker python lib
pip3 install docker-compose # docker script
pip3 install ansible  # provisioning tool
cd installer #  
# open a file vars.yml and copy and paste these 3 following lines
admin_password: 'adminpass'
pg_password: 'pgpass'
secret_key: 'mysupersecret'
# hit the command
ansible-playbook -i inventory install.yml -e @vars.yml

```