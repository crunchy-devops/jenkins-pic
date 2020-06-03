# Configure your IDE 
Set up your workspace environnement using JetBrains    
You can use IntellijIdea Community Edition     
Download the package from   
https://www.jetbrains.com/idea/download/download-thanks.html?platform=windows&code=IIC
 
## In the IDE 
Go to File -> Settings  -> Plugins 
and install Jenkins Control Plugin 
Restart IntellijIDEA
You got a right-hand side tab named Jenkins   
Click on the wrench to get the configuration dialog window
Fill Server Address, username, passwords, crumb data , jenkins version ver 2.x
Tick use green color....
![Jenkins_config](screenshots/jenkins_config_plugin.png)
### How to get the Crumb data  
Use your browser and hit  
```http://<your_ip_address>:18080/crumbIssuer/api/json?tree=crumb```  
Copy and paste the crumb token value.    

## Remove CSRF failed check 
Go to Manage Jenkins -> Script console and run the following groovy script.
```gwt javascript
import jenkins.model.Jenkins
def instance = Jenkins.instance
instance.setCrumbIssuer(null)
```

