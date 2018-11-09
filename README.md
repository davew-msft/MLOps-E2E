# Welcome to a hands-on workshop for **Machine Learning on Big Data** using Azure Databricks, Azure Data Factory, and Azure Machine Learning service

### The datasets and base notebooks were provided with data from the SQL Server 2017 Adventureworks Data Warehouse [AdventureWorksDW2017.bak](https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-2017) and the [Azure Machine Learning Notebooks](https://github.com/Azure/MachineLearningNotebooks)

![End-to-end Custom AI Solution](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/e2e.png)


## Prerequisites

To deploy the Azure resources required for this lab, you will need:

1. An [Azure account](https://portal.azure.com)
   
   `Note:` If you don't have an account you can create your free Azure account [here](https://azure.microsoft.com/en-us/free/)
2. Microsoft [Azure Storage Explorer](https://azure.microsoft.com/en-au/features/storage-explorer/)
3. Clone this GitHub repository using Git and the following commands: 

    `git clone https://github.com/DataSnowman/MLonBigData.git`

**Note** that you will be deploying a number of Azure resources into your Azure Subscription when either clicking on the [Deploy to Azure](https://github.com/DataSnowman/MLonBigData/blob/master/setup/README.md) button, or by alternatively deploying by using an ARM template and parameters file via the Azure CLI.

## Deploy Bike Buyer Template to Azure

**Important** `While Azure Data Factory Data Flows is in Preview please use Southeast Asia Region to deploy this solution

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FDataSnowman%2FMLonBigData%2Fmaster%2Fsetup%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2FDataSnowman%2FMLonBigData%2Fmaster%2Fsetup%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

Note: If you encounter issues with resources please check by running the following commands in the Azure CLI (Note more information on using the CLI is found in the `Provisioning using the Azure CLI` section below):
  
  `az login`

  `az account show`

  `az account list-locations`
  
  `az provider show --namespace Microsoft.Databricks --query "resourceTypes[?resourceType=='workspaces'].locations | [0]" --out table`

## Choices for Provisioning

You can provision using the Deploy to Azure button above or by using the Azure CLI.

### Provisioning using the Azure Portal

Choose your Subscription, and enter a Resource Group group, Location (Southeast Asia for the ADF Data Flow Preview) SQL Server Username, SQL Server Password, and agree to the Terms and Conditions. Then click the `Purchase` button.

![setup](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/setup.png)

When the Deployment completes you will receive a notification in the Azure Portal.  Click the `Go to resource group` button.

![preview](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/preview.png)

After you open the resource group in the Azure portal you should see these deployed resources

![deploy](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/deploy.png)

### Provisioning using the Azure CLI

1. Download and install the [Azure CLI Installer (MSI) for Windows](https://aka.ms/InstallAzureCliWindows) or [Mac or Linux](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) . Once the installation is complete open the command prompt and run `az login`, then copy the access code returned. In a browser, open a **private tab** and enter the URL `aka.ms/devicelogin`. When prompted, paste in the access code from above. You will be prompted to authenticate using our Azure account.  Go through the appropriate multifaction authenication.

2. Navigate to the folder `MLonBigData\setup` If using **Windows Explorer** you can launch the command prompt by going to the address bar and typing `cmd` (for the Windows command prompt) or `bash` (for the Linux command prompt assuming it is installed already) and type `az --version` to check the installation.  Look for the `parameters-mlbigdata.json` file you cloned during the Prerequisites above.  

3. When you logged in to the CLI in step 1 above you will see a json list of all the Azure account you have access to. Run `az account show` to see you current active account.  Run `az account list -o table` if you want to see all of you Azure account in a table. If you would like to switch to another Azure account run `az account set --subscription <your SubscriptionId>` to set the active subcription.  Run `az group create -n mlbigdata -l southeastasia` to create a resource group called `mlbigdata`.

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

## Data Scientist is using Anaconda and Jupyter Notebooks

If you are interested in this scenario [start here](https://github.com/DataSnowman/MLonBigData/tree/master/BikeBuyer/OriginalDataScientistWork)

## Create Azure Databricks Cluster

Launch the Azure Databricks Workspace by clicking on the `Launch Workspace` button in the Azure Portal

![launchWorkspace](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/launchWorkspace.png)

Click on `Clusters` in the left navigation bar and click on the `+ Create Cluster` button

![createCluster](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/createCluster.png)

Name your cluster, choose the Standard Cluster Mode, 4.2 Databricks Runtime Version (or newer), Python Version 3, and reduce the max workers to 3.  Click the `Create Cluster` button.

![cluster](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/cluster.png)

## Importing and running Databricks notebooks

### Importing notebooks using the dbc file

Click on `Workspace` in the left navigation bar and right-click on the user and select `Import`

![import](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/import.png)

Select the BikeBuyerOps.dbc file that was cloned from the GitHub repo. The location should be MLonBigData\BikeBuyer\ADBnotebooks Click the `Import` button

![importNotebooks](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/importNotebooks.png)


### Running the Data Engineer notebooks

### Running the Data Scientist notebooks

### Running the Notebooks loading SQL

## Connecting to Databricks and SQL Database using Power BI



Hope you enjoyed this workshop.

## Thank you to the members of Databricks that created the notebooks for this tutorial:
* **Name One** 
* **Name Two**
