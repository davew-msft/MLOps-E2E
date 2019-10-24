## Lab 23:  Test Our Pipelines

TODO


### Discussion topics before we start this section  

1. 
2. 

## Steps

### Task 1: Make Edits to Source Code

1. Navigate to: **Repos -> Files -> scripts -> train.py**.

2. **Edit** `train.py`.

3. Change the **learning rate (lr)** for the optimizer from **0.1** to **0.001**.

4. Change the number of training **epochs** from **1** to **5**.

5. Select **Commit**.

    ![Make edits to train.py by changing the learning rate. Select Commit after editing.](media/44_1.png 'Edit Train.py')
    
6. Provide comment: `Improving model performance: changed learning rate.` and select **Commit**.

    ![Provide commit comment for train.py.](media/45_1.png 'Commit - Comment')
    
### Task 2: Monitor Build Pipeline

1. Navigate to **Pipelines, Builds**. Observe that the CI build is triggered because of the source code change. 

   ![Navigate to Pipelines, Builds.](media/46_1.png 'Pipelines - Builds')
   
2. Select the pipeline run and monitor the pipeline steps. The pipeline will run for 16-18 minutes. Proceed to the next task when the build pipeline successfully completes.
    
   ![Monitor Build Pipeline. It will take around 16-18 minutes to complete.](media/47.png 'Build Pipeline Steps')

### Task 3: Monitor Release Pipeline

1. Navigate to **Pipelines, Releases**. Observe that the Release pipeline is automatically trigger upon successful completion of the build pipeline. Select as shown in the figure to view pipeline logs. 
    
   ![Navigate to Pipelines, Releases and Select as shown in the figure to view pipeline logs.](media/48.png 'Pipelines - Releases')
   
2. The release pipeline will run for about 15 minutes. Proceed to the next task when the release pipeline successfully completes.

### Task 4: Review Release Pipeline Outputs

1. From the pipeline logs view, select **Deploy & Test Webservice** task to view details.

    ![Select Deploy & Test Webservice task to view details.](media/50.png 'Pipeline Logs')
    
2. Observe the **Scoring URI** and **API Key** for the deployed webservice. Please note down both the `Scoring URI` and `API Key` for *Exercise 7*.

    ![View Deploy & Test Webservice task logs and note down the Scoring URI of the deployed webservice.](media/51.png 'Deploy & Test Webservice Task Logs')

3. Log in to Azure Portal. Open your **Resource Group, Workspace, Deployments** section, and observe the deployed webservice: **compliance-classifier-service**.

    ![View deployed webservice in Azure Portal.](media/52.png 'Azure Portal - Workspace, Deployments')




## Exercise 7: Testing the deployed solution

Duration: 15 minutes

In this exercise, you verify that the first release of the application works.

### Task 1: Test the Deployment

1. Browse to your Azure Notebooks project and navigate to `Test Deployment.ipynb`. This is the notebook you will step through executing in this lab.

2. Follow the instructions within the notebook to complete the lab.

3. Note that you will have to provide values for **Scoring URI** and **API Key** for the deployed webservice in the notebook.
 

## Exercise 8: Examining deployed model performance

Duration: 15 minutes

In this exercise you learn how to monitor the performance of a deployed model.

### Task 1: Activate App Insights and data collection on the deployed model

1. Browse to your Azure Notebooks project and navigate to the [Model Telemetry](notebooks/Model%20Telemetry.ipynb) notebook. This is the notebook you will step through executing in this task.

2. Follow the instructions within the notebook to complete the task. When finished, your deployed model has now both [Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview) integration and data collection activated.

3. Note that if there are errors (for example, `Too many requests for service compliance-classifier-service (overloaded)`) when you make calls against the deployed web service after your enable app insights (last cell in the `Model Telemetry` notebook). Please wait for 5 minutes and rerun the cell to make few calls against the deployed web service.

### Task 2: Check Application Insights telemetry

1. Navigate to the Azure Portal and locate the resource group you created for this lab (the one where the Azure Machine Learning service workspace was created in).

2. Locate the Application Insights instance in the resource group and click on it.

    ![Application Insights instance in resource group.](media/telemetry-01.png 'Resource Group Overview')

3. Go to **Overview**.

4. From the top row of the right section select **Logs (Analytics)**. This will open the Application Insights query editor with an empty new query.

    ![From Application Insights Dashboard, select Logs to open the Query Editor.](media/telemetry-02.png 'Application Insights - Dashboard')

5. In the left pane, make sure the **Schema** tab is selected. 

6. Hover over **requests** and click the icon on the right side - "Show sample records from this table". 

    ![In Application Insights create requests query.](media/telemetry-03.png 'Create Requests Query')

7. Look at the results displayed. Application Insights is tracing all requests made to your model. Sometimes, a couple of minutes are needed for the telemetry information to propagate. If there are no results displayed, wait a minute, call again your model, and click **Run** to re-execute the Application Insights query. 

   ![In Application Insights observe requests query results.](media/telemetry-04.png 'Requests Query Results')

*Note that if you do not see telemetry information after selecting **Run** to re-execute the Application insights query. Please rerun the last cell in the `Model Telemetry` notebook few more times to generate more data. Then select **Run** on this page to re-execute the Application insights query.*

### Task 3: Check the data collected

1. Navigate to the Azure Portal and locate the resource group you created for this lab (the one where the Azure Machine Learning service workspace was created in).
2. Locate the Storage Account instance in the resource group and click on it.

    ![From the Resource Group Overview locate the Telemetry Storage account](media/telemetry-05.png 'Resource Group Overview')

3. Go to **Storage Explorer (preview)**.

4. Expand the **BLOB CONTAINERS** section and identify the **modeldata** container. Select **More->Refresh** if you do not see **modeldata** container.

    ![Locate the telemetry blob container in the storage account.](media/telemetry-06.png 'Storage Explorer') 

5. Identify the CSV files containing the collected data. The path to the output blobs is based on the following structure:

    `modeldata -> subscriptionid -> resourcegroup -> workspace -> webservice -> model -> version -> identifier -> year -> month -> day -> data.csv`

    ![Locate telemetry data in the blob container.](media/telemetry-07.png 'Storage Explorer - data.csv')


## After the hands-on lab 

Duration: 5 minutes

To avoid unexpected charges, it is recommended that you clean up all of your lab resources when you complete the lab.

### Task 1: Clean up lab resources

1.  Navigate to the Azure Portal and locate the `MCW-AI-Lab` Resource Group you created for this lab.

2.  Select **Delete resource group** from the command bar.

    ![Screenshot of the Delete resource group button.](media/image71.png 'Delete resource group button')

3.  In the confirmation dialog that appears, enter the name of the resource group and select **Delete**.

4.  Wait for the confirmation that the Resource Group has been successfully deleted. If you don't wait, and the delete fails for some reason, you may be left with resources running that were not expected. You can monitor using the Notifications dialog, which is accessible from the Alarm icon.

    ![The Notifications dialog box has a message stating that the resource group is being deleted.](media/image72.png 'Delete Resource Group Notification Dialog')

5.  When the Notification indicates success, the cleanup is complete.

    ![The Notifications dialog box has a message stating that the resource group has been deleted.](media/image73.png 'Delete Resource Group Notification Dialog')

You should follow all steps provided _after_ attending the Hands-on lab.

