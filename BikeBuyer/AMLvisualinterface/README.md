# This is the scenario where the Data Scientist is using the Azure Machine Learning service Visual interface

If you are interested in this scenario [start here](https://github.com/DataSnowman/MLonBigData/tree/master/BikeBuyer/AMLvisualinterface)

![Data Science with AML Visual interface Portal](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfacePortal.png)

![Data Science with AML Visual interface](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterface.png)

## Prerequisites

To create the BikeBuyer Experiment and Model you will need:

1) [Create](https://docs.microsoft.com/en-us/azure/machine-learning/service/setup-create-workspace) an Azure Machine Learning service workspace 
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

Click on the Machine Learning service workspace.  You should now see a new choice under Authoring.  Choose Visual interface, and click Launch visual interface.

![Data Science with AML Visual interface Portal](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfacePortal.png)

The Visual interface should look like this, with Experiments, Web Services, and Datasets.  To get started click on +New

![amlVisualinterfaceStart](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceStart.png)

Choose Datasets and click the Upload from local file.

![amlVisualinterfaceNewDataset](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewDataset.png)

Click the Choose File button and navigate to the `data-scientist-model.csv` file which should be located in the path MLonBigData\BikeBuyer\OriginalDataScientistWork\data in your cloned GitHub repo.  Choose Generic CSV File with a header (.csv) and the click OK

![amlVisualinterfaceNewDataset2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewDataset2.png)

The dataset should now showup under My Datasets

![amlVisualinterfaceNewDataset3](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewDataset3.png)

Click on +New and choose Experiments, and click on Blank Experiment

![amlVisualinterfaceNewExperiment](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment.png)

Drag the `data-scientist-model.csv` dataset from Saved Datasets>My Datasets

![amlVisualinterfaceNewExperiment1](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment1.png)

Drag the Clean Missing Data module from Data Transformation>Manipulation and join the `data-scientist-model.csv` dataset to the Clean Missing Data module.  Choose Cleaning mode>Remove entire row.  Click Run

![amlVisualinterfaceNewExperiment2](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment2.png)

Create new Compute Target, provide a name and click Run

![amlVisualinterfaceNewExperiment3](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment3.png)

The experiment will start running.  The first time you run the experiment it takes time to prepare the compute.  Subsequent runs will be faster. 

![amlVisualinterfaceNewExperiment4](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment4.png)

Name the experiment `BikeBuyer` and click Save

![amlVisualinterfaceNewExperiment5](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment5.png)

Click on the Cleaned dataset port and select Visualize

![amlVisualinterfaceNewExperiment6](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment6.png)

Click on a column like Gender to see Statistics and Visualizatons

![amlVisualinterfaceNewExperiment7](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment7.png)

Close the Visualizations and drag a Split Data module from Data Transformation>Sample and Split>Split Data.  Join the Clean Missing Data module to the Split Data module.  Change the Fraction of rows in the first output from 0.5 to 0.7  

![amlVisualinterfaceNewExperiment8](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment8.png)

Add the following modules:

`Two-class Decision Forest` from Machine Learning>Initialize Model>Classification
`Train Model` from Machine Learning>Train
`Score Model` from Machine Learning>Score
`Evaluate Model` from Machine Learning>Evaluate

Join them together as in the image below

![amlVisualinterfaceNewExperiment9](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment9.png)

Click on the Train Model module and select the `BikeBuyer` column 

![amlVisualinterfaceNewExperiment10](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment10.png)

Click Save and then click Run.  Then Select existing Compute target and click Run.

![amlVisualinterfaceNewExperiment11](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment11.png)

Please checkout the [AML service documentation](https://docs.microsoft.com/en-us/azure/machine-learning/service/ui-quickstart-run-experiment) if you have questions about how to use the Visual interface

When the experiment completes, click on the Evaluation results node and select Visualize

![amlVisualinterfaceNewExperiment12](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment12.png)

You can see it is a decent Bike Buyer prediction model with an AUC of 0.802

![amlVisualinterfaceNewExperiment13](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment13.png)

Close the Evaluation results

Click `Create Predictive Experiment` on the bottom bar

When it completes a new `BikeBuyer [trained model]` is created with Web service input and output.

![amlVisualinterfaceNewExperiment14](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment14.png)

You need to click Run one more time to be able to Deploy the model as a web service.  When it completes click `Deploy Web Service`

![amlVisualinterfaceNewExperiment15](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment15.png)

Click on the `Go to Azure Portal` link

![amlVisualinterfaceNewExperiment16](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment16.png)

Click on + Add Compute

![amlVisualinterfaceNewExperiment17](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment17.png)

Provide a Compute name, select Kubernetes Service Compute Type, select Region.  Stay with the defaults for other values and click Create

![amlVisualinterfaceNewExperiment18](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment18.png)

Return to Setup Compute Target to Deploy Web Service dialog in Visual interface and change to Select existing

![amlVisualinterfaceNewExperiment19](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment19.png)

Click the Refresh in the dialog to see if the AKS service is deployed

![amlVisualinterfaceNewExperiment20](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment20.png)

Once the AKS service is created you will be able to click the Deploy button

![amlVisualinterfaceNewExperiment21](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment21.png)

While you are waiting check out:

Compute - should see Kubernetes service

![amlVisualinterfaceNewExperiment22](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment22.png)

Images - should see bikebuyeraciws

![amlVisualinterfaceNewExperiment23](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment23.png)

Deployments - should see BikeBuyer [Predictive Exp.]

![amlVisualinterfaceNewExperiment24](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment24.png)

Back in the Visual interface under Web Services you should see the same BikeBuyer [Predictive Exp.]

![amlVisualinterfaceNewExperiment25](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment25.png)

Click on the BikeBuyer [Predictive Exp.] Name.  When it opens click on Test and then the Test Button

![amlVisualinterfaceNewExperiment26](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment26.png)

This tests that the web service is working by sending input and returning output.  If you would like to test it outside of AML service Visual interface click on the API Doc

![amlVisualinterfaceNewExperiment27](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment27.png)

This has the Request URI, Authorization Token, and Sample Request Body

I use [Postman](https://www.getpostman.com/downloads/) to test. 

![amlVisualinterfaceNewExperiment28](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment28.png)

## Delete the Web Service and AKS Compute when you are finished

When you are done using the Web Service and AKS Compute go back to the Visual interface console and click on Web Services.  Select the web service name and click `Delete`.  

![amlVisualinterfaceNewExperiment29](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment29.png)

This should delete the deployment 

![amlVisualinterfaceNewExperiment30](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment30.png)

But you will need to delete the AKS compute from the Compute in the AML service workspace.  The same place where you added the Compute in previous steps above.

![amlVisualinterfaceNewExperiment31](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment31.png)

You can see if you have virtual machines running in your vms

![amlVisualinterfaceNewExperiment32](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment32.png)

Once the AKS compute is deleting you should see the VMs go away as the Kubernetes service deletes

![amlVisualinterfaceNewExperiment33](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment33.png)

![amlVisualinterfaceNewExperiment34](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/amlVisualinterfaceNewExperiment34.png)




