## Lab 1:  Workshop Setup

Discussion topics before we start this section:  

* We use `bash` and `az cli` commands throughout this lab.  What is your comfort level with bash? 
* Why do we need to do "resource prefixing"?  
* What is your preferred IDE?  I like to use vscode
* Cloud Shell overview?  Why tmux?  
* What is your git experience?  
* To speed up Azure deployments we use ARM Templates.  What is your experience?  


### Prerequisites

* We will use `bash` and `az cli` commands throughout the workshop.  You can use Powershell as an alternative, but the commands will be different.  

* You **will need** an Azure account with at least one Resource Group with owner permissions.  

> Note: If you don't have an account you can create your free Azure account [here](https://azure.microsoft.com/en-us/free/).  **But we aware that free trial accounts do not always allow every Azure service to be spun up and utilized.**


### On Your Local Laptop...

you'll likely need the following, which can be installed now or as we progress through the workshop:

* [Azure Storage Explorer](https://azure.microsoft.com/en-au/features/storage-explorer/)
* VSCode
* Clone this GitHub repository using Git and the following commands: 

    `git clone https://github.com/davew-msft/MLOps-E2E`
* I prefer to use WSL in Windows but Azure Cloud Shell is fine.  If you do NOT want to use Cloud Shell then you'll need the following:
  * [Azure CLI Installer (MSI) for Windows](https://aka.ms/InstallAzureCliWindows)
  * or the WSL/Linux version


### Deploy Resources to Azure

You need one resource group.  

* Suggested name (used throughout this workshop):  `MLOpsWorkshop`.  
* Suggested region:  `East US`.



Run the following to create the RG using Cloud Shell:

``` bash
tmux

#vars/changeme
ResGroup='MLOpsWorkshop'
Subscription='davew demo'
location='eastus'

# ensure you are connected to the desired subscription
az account list --output table
az account set --subscription "$Subscription"
az account list --output table

az group create --name $ResGroup --location $location
```

Now we need to provision our resources using the ARM templates.  

I assume Cloud Shell.  Here's the steps:  

```bash
# clone the repo first in your cloud shell
mkdir -p git && cd $_
git clone https://github.com/davew-msft/MLOps-E2E mlops
cd mlops

az group deployment create \
    -g $ResGroup \
    --template-file setup/azureclideploy.json \
    --parameters @parameters.json

    
```

4. Next run the following command to provision the Azure resources:
```
az group deployment create -g mlbigdata --template-file azureclideploy.json --parameters @parameters-mlbigdata.json
```
Once the provisioning is finished, we can run `az resource list -g mlbigdata -o table` to check what resources were launched. Our listed resources includes: 
    * 1 Storage account
    * 1 Data Factory
    * 1 Databricks workspace
    * 1 SQL Server
    * 1 SQL database.