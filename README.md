# Welcome to a hands-on workshop for **Machine Learning on Big Data** using Azure Databricks, Azure Data Factory, and Azure Machine Learning service

## `Note:` If you would like to view my presentation of this content in Beijing DevDays in November 2018 you can view it [HERE](https://1drv.ms/v/s!AmFpgz3VMIP0hqxdcm30uQvgEZd3jg)

### The datasets and base notebooks were provided with data from the SQL Server 2017 Adventureworks Data Warehouse [AdventureWorksDW2017.bak](https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-2017) and the [Azure Machine Learning Notebooks](https://github.com/Azure/MachineLearningNotebooks)

![End-to-end Custom AI Solution](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/e2e.png)


## Prerequisites

To deploy the Azure resources required for this lab, you will need:

1. An [Azure account](https://portal.azure.com)
   
   `Note:` If you don't have an account you can create your free Azure account [here](https://azure.microsoft.com/en-us/free/)
2. Microsoft [Azure Storage Explorer](https://azure.microsoft.com/en-au/features/storage-explorer/)
3. Clone this GitHub repository using Git and the following commands: 

    `git clone https://github.com/DataSnowman/MLonBigData.git`

**Note** that you will be deploying a number of Azure resources into your Azure Subscription when either clicking on the `Deploy to Azure` button below, or by alternatively deploying by using an ARM template and parameters file via the Azure CLI.

## Deploy Bike Buyer Template to Azure

**Important** `For the DevDays in Taipei please use the Southeast Asia Region to deploy this solution

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

Choose your Subscription, and enter a Resource group, Location (Southeast Asia for the DevDays in Taipei) Resource Prefix (Short Prefix of 10 characters or less for all resources created by this template so they are unique), SQL Server Username, SQL Server Password, and agree to the Terms and Conditions. Then click the `Purchase` button.

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

## Data Scientist using Anaconda and Jupyter Notebooks

If you are interested in this scenario [start here](https://github.com/DataSnowman/MLonBigData/tree/master/BikeBuyer/OriginalDataScientistWork)

![Original Data Scientist Work](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/originalDataScientistWork.png)

## Data Engineer using Azure Databricks Notebooks

If you are interested in this scenario [start here](https://github.com/DataSnowman/MLonBigData/tree/master/BikeBuyer/ADBnotebooks/DataEngineering)

![Data Engineering with Azure Databricks](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/deWithAzureDatabricks.png)

## Data Engineer using Azure Data Factory Data Flow and Azure Databricks

If you are interested in this scenario [start here](https://github.com/DataSnowman/MLonBigData/tree/master/BikeBuyer/ADF)

![deWithAzureDataFactoryDF](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/deWithAzureDataFactoryDF.png)

## Data Scientist using Azure Databricks and Databricks Notebooks and Azure Machine Learning service SDK

If you are interested in this scenario [start here](https://github.com/DataSnowman/MLonBigData/tree/master/BikeBuyer/ADBnotebooks/BikeBuyerOps)

![Data Science with Azure Databricks and AML SDK](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/dsWithAzureDatabricksAML.png)

Hope you enjoyed this workshop.
