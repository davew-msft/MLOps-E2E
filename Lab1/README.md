## Lab 1:  Workshop Setup


### Prerequisites

* We will use `bash` and `az cli` commands throughout the workshop.  You can use Powershell as an alternative, but the commands will be different.  

* You **will need** an Azure account with at least one Resource Group with owner permissions.  Suggested name (used throughout this workshop):  `MLOpsWorkshop`.  Suggested region:  `East US`.

> Note: If you don't have an account you can create your free Azure account [here](https://azure.microsoft.com/en-us/free/).  **But we aware that free trial accounts do not always allow every Azure service to be spun up and utilized.**

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

### On Your Local Laptop...

you'll likely need the following, which can be installed now or as we progress through the workshop:

* [Azure Storage Explorer](https://azure.microsoft.com/en-au/features/storage-explorer/)
* VSCode
* Clone this GitHub repository using Git and the following commands: 

    `git clone https://github.com/davew-msft/MLOps-E2E`

