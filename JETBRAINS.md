# Configure your IDE 
Set up your workspace environnement using JetBrains      
You should use Goland Jetbrains   

Download the package from   
https://www.jetbrains.com/go/download/download-thanks.html

## In the IDE 
Go to File -> Settings  -> Plugins 
and install Jenkins Control Plugin 
Restart Goland 
You got a right-hand side vertical bar tab named Jenkins   
Select the flat key of 15 in the menu bar 
Select Jenkins Server Settings... 
Fill Server Address, username, Token, http://<ip>:32500/
Enter the token previously saved in your notepad
Test connection 

## Eventually troubleshooting
Go to Manage Jenkins -> Script console and run the following groovy script.
```groovy
import jenkins.model.Jenkins
def instance = Jenkins.instance
instance.setCrumbIssuer(null)
```

## Eventually troubleshootingTroubleshooting   
if you have a message URL is mal/formed   
Go to Jenkins -> manage Jenkins-> Configuration system  
Go to Jenkins Location   
and remove the trailing /   
Press save  
and test again 


## Go to DEPLOYMENT.md file and follow the instructions.