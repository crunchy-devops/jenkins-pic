# Configure slave

## Install ssh build agent plugin and ssh agent plugins
select manage jenkins -> plugin manager -> tab available     
filter ssh type and select both plugins
and hit install without restart 

## Create a slave 
select manage jenkins -> Manage Nodes and clouds  
select on left hand side -> New Node  
Node name : slave1  
tick permanent agent  
Description : my slave  
Number of executors : 1  
remote root directory:  /home/jenkins/jenkins_slave  
labels: ubuntu_slave1  
usage: only build jobs with label expression matching this node   
Launch method: Launch agent via SSH  
Host:  <your ip address>   
Credentials: user/password  
Host key verification strategy: Non verifying verification strategy  
Availability: Keep this agent online as much as possible  