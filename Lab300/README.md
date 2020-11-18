## A Day in the Life of a Data Scientist  - The Data Science Process

You are somewhat new to data science and your boss hands you a new dataset and says, "make something out of this."  Where do you even start?  In this lab we do exactly that.  In this lab we are given a dataset of support tickets and we are told, "unlock some insights to help the support team become more efficient and provide better service to customers."  We work through how to get started on an analytics problem like this.  
    * What do we do?
      * use standard data science techniques to explore the data
      * determine deductively what are some interesting problems we can solve
      * use automl to see if we can quickly predict those problems
      * deploy the best model, assuming it meets our goals
      * present your interesting analytics to executive leadership
    * How we do it?:
      * AMLS
      * Jupyter/python/pandas/visualizations
      * automl
      * deploy an automl "no-code" container
      * consume the model's REST API 
      * Power BI for the final data presentation


## Getting Your Environment Ready

* Power BI desktop
* Azure Subscription
* AMLS service
  * Choose to Upgrade the workspace to the **Enterprise edition (Preview)** [see more information on current pricing here](https://azure.microsoft.com/en-us/pricing/details/machine-learning/) - you will need enterprise edition to complete the experiment section.

## Data Exploration/Sandboxing

We want to examine the data

* In AMLS launch your Compute instance and JupyterLab.  To create one:
    * Select 'Compute' from left pane
    * Select 'New' under 'Compute Instances'
    * Provide a 'Compute VM Name' (all lowercase)
    * Keep the default size VM provided
* select the `JupyterLab` Link
    * Enter the user folder by double clicking
    * Select the upload button and upload the files listed below in the folders listed below -- or -- clone this repo into the JupyterLab VM using the `Terminal`:
        * [data/data_train.csv](data/data_train.csv)
        * [code/explore.ipynb](code/explore.ipynb)
        * [code/deploy.ipynb](code/deploy.ipynb)
        * [code/config.json](code/config.json)


