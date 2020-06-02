# Set up selenium Tests

## Create a Jenkins Job
### Define 
if the plugin Log Parser is not present  
Go to manage-Jenkins -> Manage plugins -> Tab available -> Filter Log Parser   
Check and install without restart   

Go New Item, Name hello-world-selenium, select Maven-project  
Hit Ok  
Source Management   
Git  https://github.com/<your_repo>/hello-world-selenium.git
Root POM: pom.xml
Goals and options: test 

### Post-build Actions   
Select Console ouptut (build log) parsing  
Tick Mark build Failed on Error  
Tick Use project rule  
Path to rule file in workspace :  parserules   
parserules file contains a regex for checking if there is an error 