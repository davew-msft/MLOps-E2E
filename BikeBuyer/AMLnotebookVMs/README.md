# This is the scenario where the Data Scientist is using the Azure Machine Learning service Notebook VM

![Data Science with AML Notebook VMs 1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookVMs1.png)

![Data Science with AML Notebook VMs 2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookVMs2.png)

## Prerequisites

To run the Bike Buyer Model notebook you will need:

1) [Create](https://www.anaconda.com/download/) an Azure Machine Learning service workspace 
2) Clone this GitHub repository using Git and the following commands: 

    ```sh
    git clone https://github.com/DataSnowman/MLonBigData.git
    ```

## Create an Azure Machine Learning service workspace in the Resource Group created earlier using the Azure Portal

`Note if you already have an Azure Machine Learning service workspace the you created in another step you can just use it (no need to create another)`

Search for `Machine Learning service workspace` in the Azure Portal

![AMLserviceWorkspace](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlServiceWorkspace.png)

Click `Create`

![CreateAMLserviceWorkspace](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/createAMLserviceWorkspace.png)

File out parameters (remember to use the same Resource group and Location as your deployment)

Click `Create`

![CreateAMLserviceWorkspace2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/createAMLserviceWorkspace2.png)

Four additional services should be added to your resource group

![amlservices](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlservices.png)

Click on the Machine Learning service workspace

