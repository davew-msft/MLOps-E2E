## Lab 2a:  Getting Databricks Ready for MLOps/DevOps

Version-controlling notebooks is challenging.  In this lab we are going to wire-up our Databricks workshop to connect to our AzDO environment. We could also use [github or BitBucket](https://medium.com/@cprosenjit/azure-databricks-version-management-35fc78e11d7#targetText=Azure%20Databricks%20Configuration&targetText=Integrate%20Azure%20Databricks%20with%20Azure,extra%20authentication%20to%20be%20supplied.&targetText=2.2%20Select%20a%20Notebook%2C%20click,and%20input%20path%20as%20appropriate.). 

### Discussion topics before we start this section  

* What is databricks?  Basic navigation of the workspace
* git integration
* notebook walkthrough
* navigating a notebook

## Spin up a Cluster

It can be as small as possible.  You don't need to wait for this to complete.  


## "Clone" this repo into AzDO 

We want to utilize the ipynb files that already exist in this repo, in DBX.  And we want to version control them appropriately.  

1.  Create a repo in AzDO
1.  on your laptop (or cloud shell), add this new "remote" to your repo and push the latest code.  

Something like this, but you may need to add "alternate credentials" first:

```bash
git remote add azdo https://gitclone@dev.azure.com/davewentzel/MLOps-E2E/_git/MLOps-E2E
git push -u azdo --all

```

1. Open DBX, go to User Settings, choose `AzDO` as the Git provider.  


## Version Controlling Notebooks - PRACTICE

...is not easy.  

You will need to follow these steps generally:

* Import an existing notebook into dbx
* Under Revision History link it to **a new folder** in AzDO.  
  * Don't use DBXNotebooks.  Consider using just `Notebooks` folder

Take some time and load all of the ipynb notebook files from DBXNotebooks into databricks, and then sync them to your AzDO repo.  Ensure you can make changes and commit them back to AzDO as you work.  


## Ensure the AML SDK is installed in your workspace/cluster

Load, run, and save to AzDO:  01.Installation_and_Configuration.ipynb



