# Configure your IDE 
Set up your workspace environnement using JetBrains    
You can use IntellijIdea Community Edition     
Download the package from
 
## In the IDE 
Go to File -> Settings  -> Plugins 
and install Jenkins Control Plugin 
You got a right-hand side tab named Jenkins   
Click on the wrench to get the configuration dialog window
![Jenkins_config](screenshots/jenkins_config_plugin.png)
### How to get the Crumb data 
use your browser and hit  
```http://<your_ip_address:18080/crumbIssuer/api/json?tree=crumb```  
Copy and paste the crumb token value  

## Remove CSRF check 
Go to Manage Jenkins / Script console and run this groovy script
```gwt javascript
import jenkins.model.Jenkins
def instance = Jenkins.instance
instance.setCrumbIssuer(null)
```

