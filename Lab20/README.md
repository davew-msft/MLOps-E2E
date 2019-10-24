## Lab 20:  Setup Azure DevOps

This lab assembles all of the pieces needed in AzDO to be ready to deploy an ML model using MLOps principles.  


### Discussion topics before we start this section  

1. Explain the starter repo


## Steps

1. Create a new AzDO project called `mlops-quickstart`.
1. Within the new project: Select **Repos** and **Import**
2. Provide the following GitHub URL: 

`https://github.com/solliancenet/mcw-mlops-starter` 

3. Select and open the `azure-pipelines.yml` file.

2. Select **Edit** and update the `variables:` accordingly.  

**You will need to work with your data scientist to determine the name of the experiment.** It _might_ be `deep-learning`.  

5. Commit your change.  


### Create new Service Connection

1. From the left navigation select **Project settings** and then select **Service connections**.
2. Select **New service connection** and then select **Azure Resource Manager**.


3. Provide the following information in the `Add an Azure Resource Manager service connection` dialog box and then select **Ok**:
 
   a. Connection name: `<Your Subscription Name>`
   
   b. Subscription: Select the Azure subscription to use.
  
   c. Resource Group: This value should match the value you provided in the `azure-pipelines.yml` file.
   
    ![Provide connection name, and Azure Resource Group and then select Ok. The resource group should match the value you provided in the YAML file.](../images/09.png 'Add an Azure Resource Manager service connection dialog')

