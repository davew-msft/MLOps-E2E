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

## Author an Azure Data Factory Data Flow


authorAndMonitorDataFactory.png

clickPencil.png

createConnections.png

blobLinkedService.png

blobLinkedServiceCfg1.png

blobLinkedServiceCfg2.png

## Create Azure Databricks Cluster (or use the one you already created in the Data Engineering step that uses the Ingest.ipynb)

Launch the Azure Databricks Workspace by clicking on the `Launch Workspace` button in the Azure Portal

![launchWorkspace](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/launchWorkspace.png)

Go to User Settings

![userSettings](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/userSettings.png)

![generateNewToken](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/generateNewToken.png)

![launchWorkspace](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/generateNewTokenDialog.png)

![copyToken](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/copyToken.png)

![tokenCreated](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/tokenCreated.png)

![databricksLinkedService](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/databricksLinkedService.png)

![databricksLinkedServiceCfg1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/atabricksLinkedServiceCfg1.png)

![databricksLinkedServiceCfg2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/databricksLinkedServiceCfg2.png)

![connectionsCreated.](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/connectionsCreated.png)