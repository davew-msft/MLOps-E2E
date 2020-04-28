## Lab 20:  Setup Azure DevOps

This lab assembles all of the pieces needed in AzDO to be ready to deploy an ML model using MLOps principles.  

Creating MLOps pipelines can be a little tough.  Luckily there is a starter repo that can help you with the scaffolding:  

`https://github.com/solliancenet/mcw-mlops-starter` 

Take a few minutes to familiarize yourself with some of the code.  I have already built/merged this code into our repo.  You can use this in the future as the basis for your own MLOps pipelines.  

If you want to merge the starter repo into your code (or you want to update this repo) then follow these steps. (There's probably an easier way to do this). :

```bash
git clone https://github.com/solliancenet/mcw-mlops-starter
rm -rf mcw-mlops-starter/.git/
rm -rf mcw-mlops-starter/README.md 
cp -R mcw-mlops-starter/. MLOps-E2E/
# now check to ensure we aren't overwriting any of our custom changes
rm -rf mcw-mlops-starter/
```

### Discussion topics before we start this section  

1. Explain the starter repo


## Steps

1. Navigate to your Azure Repo in AzDO for this repo.  
1. Select and open the `azure-pipelines.yml` file.

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

Click OK and then go back in to Update and `Verify Connection`.  