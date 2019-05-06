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

Click on the Machine Learning service workspace.  You should now see a new choice under Authoring.  Choose Notebook VMs

![amlServiceWorkspaceOverview](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlServiceWorkspaceOverview.png)

Click on +New

![amlNotebookVMsConsole](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookVMsConsole.png)

Enter an Name for the Notebook VM, choose a VM size, and click create

![amlNotebookVMsCreate](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookVMsCreate.png)

Notice how the status is `Creating`.  This is where you can go to Stop, Start, Restart, Delete, or Create Notebook VMs

![amlNotebookVMsConsole2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookVMsConsole2.png)

After a few minutes the Status will change to `Running`.  Now you can click on the URI link `Jupyter`

![amlNotebookVMsConsole3](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookVMsConsole3.png)

This will open the Jupyter Notebook Server.  Navigate to your user folder. Click on Upload and navigate to the `Bike Buyer Model.ipynb` file that you cloned earlier.  Find in MLonBigData\BikeBuyer\OriginalDataScientistWork 

![amlNotebookVMsUpload](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookVMsUpload.png)

Click on the blue Upload button.  Then click on the `Bike Buyer Model.ipynb` notebook to open it.  

![amlNotebookVMsUpload2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookVMsUpload2.png)

The notebook should look like this.

![bikeBuyerModelipynb.png](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/bikeBuyerModelipynb.png)

Create a new folder by clicking on New>Folder

![amlNotebookNewFolder](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookNewFolder.png)

This creates an Untitled Folder.  Click in the box and click Rename.  Rename the folder `data`

![amlNotebookRenameFolder](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookRenameFolder.png)

Open the data folder and click the Upload button to navigate to the `data-scientist-model.csv` file which should be located in the path MLonBigData\BikeBuyer\OriginalDataScientistWork\data in your cloned GitHub repo

![amlNotebookUploadData](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookUploadData.png)

Click on the blue Upload button. 
![amlNotebookUploadDataBlue](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookUploadDataBlue.png)

Navigate up one level in Jupyter and then click on the `Bike Buyer Model.ipynb` notebook to open it again.  Click on the Cell menu and choose `Run All` 

![amlNotebookRunAll](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookRunAll.png)

`Note that you can also upload the file using the terminal (vs the GUI upload above) in Juypter and a command like this`

```sh
wget https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/BikeBuyer/OriginalDataScientistWork/data/data-scientist-model.csv  -o /data/data-scientist-model.csv 
```

The pkl file `SupportVectorClassifier_20181104.pkl` should be created 

![amlNotebookPklModel](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookPklModel.png)

## Stop the Notebook VM

When you are done using the Notebook VM go back to the Notebook VMs console and click `Stop`.  You can return here to start it again, but this way you are not charged for compute while it is not being used.

![amlNotebookVMsConsole3Stop](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlNotebookVMsConsole3.png)