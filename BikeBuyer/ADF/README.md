# This is the scenario where the Data Engineering is being done using Azure Data Factory Data Flow and Azure Databricks

![Original Data Scientist Work](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/deWithAzureDataFactoryDF.png)

## Upload Source Files to Blob

Create a Blob containers

![CreateContainer](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/createContainer.png)

Create one called `sourcedata`

![containerSourceData](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/containerSourceData.png)

Create another called `outputdata`

![containerOutputData](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/containerOutputData.png)

Uploaded the `adworks-bike-purchases.csv` and `potential-bike-buyers.csv` files into a folder called `bikes` from the cloned repo at the path MLonBigData\BikeBuyer\LoyaltyCardBuyers

![uploadFilestobikes](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/uploadFilestobikes.png)

Here is the `bikes` folder

![blobSourceData](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/blobSourceData.png)

Here are the files inside of the `bikes` folder

![blobSourceDataFiles](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/blobSourceDataFiles.png)

## Create an Azure Data Factory V2 with Data Flow

Create a Data Factory in the Azure Portal

![createADF](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/createADF.png)


![createADF2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/createADF2.png)


![adfResources](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/adfResources.png)


## Author an Azure Data Factory Data Flow

Click on Author & Monitor

![authorAndMonitorDataFactory](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/authorAndMonitorDataFactory.png)

Click on the pencil (edit) icon

![clickPencil](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/clickPencil.png)

Click on Connections on the bottom of the left navigation panel.  Click on `+ New`

![createConnections](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/createConnections.png)

Click on the Data Store Linked Service and select `Azure Blob Storage`.  Click on `Continue`

![blobLinkedService](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/blobLinkedService.png)

Type in a name for the new Linked Service.  Choose AutoResolveIntegrationRuntime, Use Account key, Connection String, and From Azure subscription

![blobLinkedServiceCfg1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/blobLinkedServiceCfg1.png)

Select your Azure Subscription, and Storage account name.  Click `Test` and then `Finish`

![blobLinkedServiceCfg2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/blobLinkedServiceCfg2.png)

### Create Azure Databricks Cluster (or use the one you already created in the Data Engineering step that uses the Ingest.ipynb)

Launch the Azure Databricks Workspace by clicking on the `Launch Workspace` button in the Azure Portal

![launchWorkspace](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/launchWorkspace.png)

Go to User Settings

![userSettings](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/userSettings.png)

Click `Generate New Token`

![generateNewToken](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/generateNewToken.png)

Create a Comment to identify the token.  Click `Generate`

![launchWorkspace](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/generateNewTokenDialog.png)

Copy and paste the token somewhere safe to keep.  You will need it in a bit to configure a Databricks Compute Linked Service.  Click `Done`

![copyToken](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/copyToken.png)

You can now see the created token

![tokenCreated](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/tokenCreated.png)

Return to ADF Connections on the bottom of the left navigation panel.  Click on `+ New`  
Click on the Compute Linked Service and select `Azure Databricks`.  Click on `Continue`

![databricksLinkedService](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/databricksLinkedService.png)

Type in a name for the new Linked Service.  Choose AutoResolveIntegrationRuntime, From Azure subscription, Azure Subscription, and Databricks Workspace.

![databricksLinkedServiceCfg1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/databricksLinkedServiceCfg1.png)

Select New job cluster, Access token, and paste in the Access token you created above.  Choose a Cluster version, Cluster node type, Python Version, and Fixed or Outscaling worker option. Click `Test` and then `Finish`

![databricksLinkedServiceCfg2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/databricksLinkedServiceCfg2.png)

You should now see your two new Linked Services

![connectionsCreated.](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/connectionsCreated.png)

### Create Datasets

### Create Data Flow

### Create Pipeline