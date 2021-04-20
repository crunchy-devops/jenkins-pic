# Petclinic Project 
Using your experience with hello-world , build a same sort of pipeline for the Petclinic Project. 

## Step 1 --  Maven Project and save artifact
Click on new item enter a name petclinic    
Go down and copy from :  hello_world_maven   
click ok   
Replace the git repo with your repo spring-framework-petclinic
```
  https://github.com/<your_repo>/spring-framework-petclinic.git 
```
Remove for the time being, build other project in Post-build actions 
Hit Build now and check 

## Step 2 --  Q/A with SonarQube 
Click on new item enter a name petclinic-sonar    
Go down and copy from :  hello_world_sonar
click ok   
Replace the git repo with your repo spring-framework-petclinic
```
  https://github.com/<your_repo>/spring-framework-petclinic.git 
```
Remove for the time being, build other project in Post-build actions   
Hit Build now and check  
Check the result in sonar website , so you can see other metrics

## Step 3 --  Publish Artifacts in Nexus 
Click on new item enter a name petclinic-nexus      
Go down and copy from :  hello_world_nexus  
replace  
Project name : petclinic   
Group: org.springframework.samples  
artifact: spring-framework-petclinic  
Version: 1.0  
File Path: target/petclinic.war  
Remove for the time being, build other project in Post-build actions     
Hit Build now and check  
Check the result in nexus website , so you can see the war file saved.

## Step 4 --  docker Build with the artifact
 Click on new item enter a name petclinic-docker-build      
 Go down and copy from :  hello_world_docker_build
 click ok   
 Replace the git repo with your repo spring-framework-petclinic
  ```
    https://github.com/<your_repo>/spring-framework-petclinic.git 
  ```
In Execute shell replace 
```shell script
rm -Rf spring-framework-petclinic-1.0.war
wget http://nexus:8081/repository/maven-releases/org/springframework/samples/spring-framework-petclinic/1.0/spring-framework-petclinic-1.0.war -O ${WORKSPACE}/petclinic.war
docker build -t petclinic:latest .
```
 Remove for the time being, build other project in Post-build actions   
  Hit Build now and check   
  
## Step 5 --  docker Test 
 Click on new item enter a name petclinic-docker-run      
 Go down and copy from :  hello_world_docker_run
 click ok   
 In Execute shell replace
 ```shell script
  CONTAINER_NAME="petclinic-test"
  OLD="$(docker ps --all --quiet --filter=name="$CONTAINER_NAME")"
  if [ -n "$OLD" ]; then
    docker rm -f $OLD
  fi
  docker run -d --name petclinic-test -p 9090:8080 petclinic
 ```
 Remove for the time being, build other project in Post-build actions  
   Hit Build now and check   
  Check by opening your browser    
  ```shell script
     http://<ip_address>:9090/petclinic
``` 

  ## Step 6 -- Set up JMeter test 
  go to JMETER.md file,  see the PART PETCLINIC PROJECT  
  Click on new item enter a name petclinic-jmeter   
  Go down and copy from :  hello_world_jmeter   
  click ok  
  Replace the git repo with your repo spring-framework-petclinic  
   ```
     https://github.com/<your_repo>/spring-framework-petclinic.git 
   ``` 
   In Execute shell replace  
   ```shell script
   jmeter -Jjmeter.save.saveservice.output_format=xml -Jjmeter.save.saveservice.response_data.on_error=true -n -t petclinic_test_plan.jmx  -l testresult.jlt
   ```
  Add performance plugin 
  
   ## Step 7 -- Define petclinic pipeline 
  Go to  petclinic job     
  Configure        
  Post build actions Select build other projects   
 type petclinic-sonar   
 Do the same with  
 petclinic-sonar   
 petclinic-nexus  
 petclinic-docker-build  
 petclinic-docker-test  
 petclinic-jmeter  
 Clich on the tab + in the dashboard screen   
 Enter view name petclinic pipeline 
 tick build pipeline view  
 press ok   
 Enter petclinic in select initial job   
 press apply and save   
 Check the pipeline graph   
 Hit run  
 Add webhook on spring-framework-petclinic github 
 and set webhook trigger in petclinic