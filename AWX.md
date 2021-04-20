# AWX 17.1.0
```shell
cd 
git clone https://github.com/ansible/awx.git
cd awx 
git checkout 17.1.0
python3 -m venv venv
source venv/bin/activate
pip3 install wheel
pip3 install requests
pip3 install docker
pip3 install docker-compose
pip3 install ansible
cd installer
# open a file vars.yml
admin_password: 'adminpass'
pg_password: 'pgpass'
secret_key: 'mysupersecret'
ansible-playbook -i inventory install.yml -e @vars.yml

```