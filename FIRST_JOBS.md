# Change admin password 
click on admin in a left upper right hand side of a screen  
Hit configure  
and change the password by pressing    

# First jobs
We are going to set up our first jobs    

## Hello world 
Go to jenkins, select New Items  
Type a name, hit freestyle and OK    
select build Execute a shell  

## install github plugin and maven plugin   
manage jenkins -> plugin manager       
filter github and select github integration  
filter maven and select maven integration     
and hit install without restart  

go to manage jenkins -> global tool configuration 
Maven -> add maven    
Name Maven 3.6.3  
install from Apache select version 3.6.3  

## Hello world using Maven 
New Item -> maven project and ok 
select git as a source 
https://github.com/crunchy-devops/hello-world.git  
Build uses a pom.xml file   
Goals are: clean install package  

## Hello world under Sonar 
manage jenkins -> plugin manager       
filter sonar and select Sonarqube Scanner  
and install without restart  
Go to manage jenkins -configuration   
Sonarqube server   
Tick enable injection  
Name SonarQube  
ServerURL:  http://sonar:9000  
Create a credential   
Got to  
Type ```http://<your_ip_address:19000>`` in your browser    
Login using user: admin  password : admin  
Go to adminstration, security , user, token  
Type a name and generate    
Copy the token in the credential as a secret text   
Set an ID text for this credential  
and a description  
 
Hit New Item, Freestyle, enter a name hello-world-sonar
Tick git and enter the URL   
Tick in build environment 'Prepare SonarQube Scanner ...'  
Goals are : clean package sonar:sonar -Dsonar.host_url=$SONAR_HOST_URL  

## How to check code quality in Sonar
Type ```http://<your_ip_address:19000>`` in your browser  
Login using user: admin  password : admin  
See the result in the project  
 
## Deploy your code to Nexus
Go to your first maven build and select post build actions  
select archive the artifacts, in files to archive type **/*.war
Build now this job again 
