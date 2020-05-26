# Jmeter tests
Install Jmeter on your localhost  

## Create a test plan for Hello-world web site
Install Jmeter on your localhost, start JMeter and create the following test plan.  

![Jmeter TestPlan](screenshots/test_plan.png)

Add the JMeter global variables in the test plan screen
![Jmeter_TestPlan_variables](screenshots/test_plan_variables.png)

And Http_request_defaults_values as respectively ${IP} and ${PORT}
![Jmeter_http_request_defaults](screenshots/http_request_defaults_values.png)
 
Save this test plan in your github repo project, it's jmx file 

## Recording a test plan for Petclinic website
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


