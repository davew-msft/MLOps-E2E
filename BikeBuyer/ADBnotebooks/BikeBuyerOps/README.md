# This is the scenario where the Data Science is being done using Azure Databricks and the Azure Machine Learning service SDK

![Data Science with Azure Databricks and AML SDK](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/dsWithAzureDatabricksAML.png)

## Create an Azure Machine Learning service Workspace in the Reasource Group created earlier

![AMLserviceWorkspace](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlServiceWorkspace.png)

![CreateAMLserviceWorkspace](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/createAMLserviceWorkspace.png)

![CreateAMLserviceWorkspace2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/createAMLserviceWorkspace2.png)

You will need to enter these AML service Workspace Parameters into Cmd 5 of the 01.Installation_and_Configuration notebook.

![AMLserviceWorkspaceParameters](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlServiceWorkspaceParameters.png)

![AMLserviceWorkspaceParametersCmd5](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlServiceWorkspaceParametersCmd5.png)

Note that you will need to install the AML service SDK as a library 

Install SDK as a library (Mandatory)
Now we support installing AML SDK as library from GUI. When attaching a library follow [this](https://docs.databricks.com/user-guide/libraries.html) and add the below string as your PyPi package (during private preview). You can select the option to attach the library to all clusters or just one cluster.

Provide this full string to install the SDK:

`azureml-sdk[databricks]`

## Create Azure Databricks Cluster (or use the one you already created in the Data Engineering step that uses the Ingest.ipynb)

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

### Run the 5 notebooks in order starting with 01.Installation_and_Configuration.ipynb and finishing with 05.Bike_Buyer_Deploy_to_AKS_existingImage.ipynb