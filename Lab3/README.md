## Lab 3:  Azure Machine Learning Services

### Discussion topics before we start this section  


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

Name your cluster, choose the Standard Cluster Mode, 5.2 Databricks Runtime Version (or newer), Python Version 3, Terminate after 
60 minutes of inactivity, and reduce the max workers to 3.  Click the `Create Cluster` button.

![cluster](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/cluster.png)

## Importing and running Databricks notebooks

### Importing notebooks using the dbc file

Click on `Workspace` in the left navigation bar and right-click on the user and select `Import`

![import](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/import.png)

Select the BikeBuyerOps.dbc file that was cloned from the GitHub repo. The location should be MLonBigData\BikeBuyer\ADBnotebooks Click the `Import` button

![importNotebooks](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/importNotebooks.png)

### Install azureml-sdk

Click on `Workspace` in the left navigation bar and right-click on the user and select `Create>Library`.  Choose PyPI and paste `azureml-sdk[databricks]` into the Package, and click Create

![amlsdklibrary](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlsdklibrary.png)

Click the Install automatically on all clusters check box

![amlsdklibrary2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlsdklibrary2.png)

It should install and eventually have a Installed Status

### Run the 5 notebooks in order starting with 01.Installation_and_Configuration.ipynb and finishing with 05.Bike_Buyer_Deploy_to_AKS_existingImage.ipynb

Navigate to the imported notebooks. Click on `Workspace` in the left navigation bar and click on the user>BikeBuyerOps> 01.Installation_and_Configuration

![notebooks](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/notebooks.png)

Enter these AML service workspace Parameters into Cmd 5

![AMLserviceWorkspaceParametersCmd5](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlServiceWorkspaceParametersCmd5.png)

Run Cmd 4

Run Cmd 5

Run Cmd 6 to Authenticate to Azure (will user browser and code) via Azure SDK

Run the remainder of the cells

Click on `Workspace` in the left navigation bar and click on the user>BikeBuyerOps> 02.Bike_Buyer_Ingest

Add a cell just below Cmd 3 Data Injestion

Cut and paste the following import statements

import os

import urllib

![addCell](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/addCell.png)

Click on Run All

This will run all of the cells in the notebook

Click on `Workspace` in the left navigation bar and click on the user>BikeBuyerOps> 03a.Bike_Buyer_Build_model

Click on Run All

Click on `Workspace` in the left navigation bar and click on the user>BikeBuyerOps> 03b.Bike_Buyer_Build_model_runHistory

Click on Run All

Click on `Workspace` in the left navigation bar and click on the user>BikeBuyerOps> 04.Bike_Buyer_Deploy_to_ACI

In Cmd 14 Comment out `myservice.delete()` so it does not delete the image created in this notebook

`#comment to not delete the web service`

`#myservice.delete()`

Click on Run All

Click on `Workspace` in the left navigation bar and click on the user>BikeBuyerOps> 05.Bike_Buyer_Deploy_to_AKS_existingImage

In Cmd 12 Comment out `#aks_service.delete()` and `aks_target.delete()` so it does not delete the image created in this notebook

`#comment to not delete the web service`

`#aks_service.delete()`

`#image.delete()`

`#model.delete()`

`#aks_target.delete()`

Click on Run All

For clean up the AKS cluster by deleting the compute resources under the Compute area of the AML service workspace
