# This is the scenario where the Data Engineering is being done using Azure Databricks Notebooks

![Data Engineering with Azure Databricks](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/deWithAzureDatabricks.png)

## Create Azure Databricks Cluster

In the Azure portal click on the Azure Databricks Service

![deploy](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/deploy.png)

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

Select the Ingest.ipynb file that was cloned from the GitHub repo. The location should be MLonBigData\BikeBuyer\ADBnotebooks\DataEngineering Click the `Import` button

![importNotebooks](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/importJupyterNotebooks.png)

### Run the Ingest.ipynb notebook

Select `Run All` to run all the cells in the Ingest Notebook

![IngestNotebook](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/ingestnotebook.png)
