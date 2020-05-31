# JMeter tests
Install JMeter on your localhost  

## Create a test plan for Hello-world website
Install Jmeter on your localhost, start JMeter and create the following test plan.  

![Jmeter TestPlan](screenshots/test_plan.png)  
Start with your mouse over test plan and right click on it.  
 menu  Add -> Config Element -> HTTP Request Defaults  
Start with your mouse over test plan and right click on it.    
 menu  Add -> Thread -> Thread Group  
Start with your mouse over Thread group and right click on it.  
menu Add -> Sampler ->  Http request  
Start with your mouse over Http request and right click on it.  
menu Add -> Assertions ->  Reponse assertion  
Start with your mouse over Thread Group and right click on it.  
menu Add -> Listener->  View Results Tree  

Click on Response action  
In Pattern to Test  click Add and enter AFIP   
Click on HTTP Request  
In Server Name or IP: < vm_ip_address>   
Port Number : 8090  
Path: /webapp  
Click on View Results Tree   
and press the green triangle in the menu bar   

Add the JMeter global variables in the test plan screen    
Click on Add , click on the left part of the line, type IP  
in right part of a line ${__P(IP,<our_ip>)}  
Click again on Add, click on the left part of the line, type PORT  
in right part of a line${__P(PORT,8090)}  

![Jmeter_TestPlan_variables](screenshots/test_plan_variables.png)

And Http_request_defaults_values as respectively ${IP} and ${PORT}
![Jmeter_http_request_defaults](screenshots/http_request_defaults_values.png)
 
Save this test plan in your github repo project, it's jmx file 

## Create a Jmeter Jenkins Job
go to new Item  type hello_world_jmeter 
copy from  hello_world_docker_build 
Remove all code in Build  Execute build and copy/paste
```shell script 
jmeter -Jjmeter.save.saveservice.output_format=xml -Jjmeter.save.saveservice.response_data.on_error=true -n -t jmeter_test_plan.jmx  -l testresult.jlt
```

### Add a Post-build actions 
### Add a plugin
Go to manage-Jenkins -> Manage plugins -> Tab available -> Filter Log Parser 
Check and install without restart   

### Parserules   
Select Console ouptut (build log) parsing  
Tick Mark build Failed on Error  
Tick Use project rule  
Path to rule file in workspace :  parserules    


##FOR PETCLINIC PROJECT
### Recording a test plan for Petclinic website
Install Firefox and download an add-on named FoxyProxy  
In foxyproxy added a proxy  
Enter a title Jmeter  
Proxy Type is HTTP    
Proxy IP is localhost  
Port is 8888  
no username or password  

![FoxyProxy](screenshots/foxyproxy.png)

### Create Test plan
Righ click on Test plan -> Add -> Non-test-elements -> HTTPS Test Script Recorder

![FoxyProxy](screenshots/Test_recorder.png)  

Click on tab Request Filtering  
Click Add in URL Patterns to Exclude   
Copy and paste these excluded files    
```shell script
   .*\.(txt|bmp|css|js|gif|ico|jpe?g|png|swf|woff|woff2|ttf).*
```

## Create a Jenkins Job
### Define 
Go to manage-Jenkins -> Manage plugins -> Tab available -> Filter Log Parser 
Check and install without restart   

Go New Item, Name hello-world-jmeter  
Source Management   
Git  https://github.com/<your_repo>/hello-world.git
Build  
Execute shell copy /paste  
```shell script 
jmeter -Jjmeter.save.saveservice.output_format=xml -Jjmeter.save.saveservice.response_data.on_error=true -n -t jmeter_test_plan.jmx  -l testresult.jlt
```
### Post-build Actions   
Select Console ouptut (build log) parsing  
Tick Mark build Failed on Error  
Tick Use project rule  
Path to rule file in workspace :  parserules    

### Performance Plugin 
Go to manage-Jenkins -> Manage plugins -> Tab available -> Filter Performance Plugin   
Check and install without restart   

Select Publish Performance test result report  
Source data files :  testresult.jlt  
![Jenkins_perf](screenshots/performance_trend.png)  


