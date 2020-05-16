# First jobs
We are going to set up our first jobs   

## Hello world 
Go to jenkins, select New Items  
Type a name, hit freestyle and OK  
select build Execute a shell  


## Hello world Maven 
select git as a source 
https://github.com/crunchy-devops/hello-world.git  
Build uses a pom.xml file   
Goals are: clean install package  

## Hello world under Sonar 
Hit New Item, enter a name hello-world-sonar  
Tick in build environment 'Prepare SonarQube Scanner ...'  
Goals are : clean package sonar:sonar -Dsonar.host_url=$SONAR_HOST_URL

## How to check code quality in Sonar
Type ```http://<your_ip_address:19000>`` in your browser  
Login using user: admin  password : admin  
See the result in the project  
 
## Deploy your code to Nexus
