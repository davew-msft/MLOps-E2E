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

Enter a unique Name, select your Subscription, use existing Resource Group and select the Resource Group created earlier by the ARM template.  Choose V2 with data flow (preview), and Southeast Asia Location.  Click `Create`

![createADF2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/createADF2.png)

The Data Factory (V2) should show up in your Resource group once the deployment is completed

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

Click the + next to Filter Resources to Add New Factory Resource and select `Dataset`

![addNewFactoryResource1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/addNewFactoryResource.png)

Select Azure Blob and click `Finish`

![newBlobDataset1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/newBlobDataset.png)

Name the dataset `Purchases`, select the AzureBlobStorage Linked service.  Browse to the `adworks-bike-purchases.csv` file in MLonBigData\BikeBuyer\LoyaltyCardBuyers.  Scroll down and check the box `Column names in the first row`. Test Connection.  It should look like this.

![datasetPurchases](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/datasetPurchases.png)

Click the Schema tab add click `Import Schema`

![importSchema1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/importSchema.png)

Select Azure Blob and click `Finish`

![newBlobDataset2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/newBlobDataset.png)

Name the dataset `PotentialBuyers`, select the AzureBlobStorage Linked service.  Browse to the `potential-bike-buyers.csv` file in MLonBigData\BikeBuyer\LoyaltyCardBuyers.  Scroll down and check the box `Column names in the first row`.  Test Connection.  It should look like this.

![datasetPotentialBuyers](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/datasetPotentialBuyers.png)

Click the Schema tab add click `Import Schema`

![importSchema1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/importSchema.png)

Select Azure Blob and click `Finish`

![newBlobDataset3](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/newBlobDataset.png)

Name the dataset `OutputDataBikes`, select the AzureBlobStorage Linked service.  Enter a file path of `outputdata/bikes`.  The file has not been created yet so you can't point to anything. Test Connection.  It should look like this.

![datasetOutputDataBikes](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/datasetOutputDataBikes.png)

Click on `Publish All`

![datasetsPublish](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/datasetsPublish.png)

### Create Data Flow

Click the + next to Filter Resources to Add New Factory Resource and select `Data Flow`.  Type `Buyers` as the Output stream name, and select `PotentialBuyers` as the Source Dataset

![buyersDataflow1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/buyersDataflow1.png)

Click on the Define Schema tab and click `Import from dataset`

![buyersDataflow2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/buyersDataflow2.png)

Type `Purchases` as the Output stream name, and select `Purchases` as the Source Dataset

![purchasesDataflow1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/purchasesDataflow1.png)

Click on the Define Schema tab and click `Import from dataset`

![purchasesDataflow2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/purchasesDataflow2.png)

Click on the + sign in front of the `Buyers` Source and select `Join`

![joinDataflow1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/joinDataflow1.png)

Type `JoinLoyaltyCardID` as the Output stream name, Left stream should default to `Buyers`, select `Purchases` for Right stream, Join type Full outer, and Join conditions `LoyaltyCardID = LoyaltyCardID` 

![joinDataflow2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/joinDataflow2.png)

Click on the + sign in front of the `JoinLoyaltyCardID` Join and select `Select`

![selectDataflow1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/selectDataflow1.png)

Name the Output stream name `SelectColumns` and select the 13 columns in the image below

![selectDataflow2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/selectDataflow2.png)

Click on the + sign in front of the `SelectColumns` Select and select `Derived Column`

![derivedColumnDataflow1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/derivedColumnDataflow1.png)

Name the `BikesTrans` Output stream name the following 8 columns and use these formulas:

`BikesTrans` --> `iif(isNull(Bikes), 0, 1)`

`MaritalStatusTrans` --> `iif(MaritalStatus == 'S', 1, 2 )`

`GenderTrans` --> `iif(Gender == 'M', 1, 2)`

`EducationTrans` --> `case(Education == 'High School', 1, Education == 'Partial College', 2, Education == 'Partial 1', 3, Education == 'Bachelors', 4, Education == 'Graduate Degree', 5, 0)`

`CommuteDistanceTrans` --> `case(CommuteDistance == '0-1 Miles', 1, CommuteDistance == '1-2 Miles', 2, CommuteDistance == '2-5 Miles', 5, CommuteDistance == '5-10 Miles', 10, 0)`

`RegionTrans` --> `case(Region == 'United States', 1, Region == 'Canada', 1, Region == 'Germany', 2, Region == 'France', 2, Region == 'United Kingdom', 2, Region == 'Australia', 3, 0)`

`AgeTrans` --> `toInteger(toInteger((currentDate() - toDate(BirthDate)))/365)`

`BikeBuyerTrans` --> `iif(isNull(Bikes ), 0, 1)`

![derivedColumnDataflow2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/derivedColumnDataflow2.png)

Click on the + sign in front of the `BikesTrans` Dervived Column and select `Sink`

![sinkDataflow1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/sinkDataflow1.png)

Name the Output stream name `BikeOutput` and chose `OutputDataBikes` Sink Dataset

![sinkDataflow2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/sinkDataflow2.png)

Map the Input to the following Outputs

![sinkMap](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/sinkMap.png)

Click on `Publish All`

![publishAll](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/publishAll.png)


### Create Pipeline

Click the + next to Filter Resources to Add New Factory Resource and select `Pipeline`.  Type `BikesPL` as the Output stream name, and fill out the Settings as follows:

![pipelineBikePL](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/pipelineBikePL.png)

Publish All and then click `Trigger Now` and `Finish`

![triggerNow](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/triggerNow.png)

If you look in your Databricks Cluster you will be able to see the job.

![jobRunningOnCluster](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/jobRunningOnCluster.png)