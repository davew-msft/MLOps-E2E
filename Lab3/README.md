## Lab 3:  Build and Deploy an ML Model

We are going to look at some sample data for a fictitious company that sells bicycles.  We have a dataset of consumers with decisions as to whether they bought or did not buy a bike.  We're going to use that data to build a predictive model and show the steps to train, test, and deploy the model using some of the services we've deployed so far.  

### Discussion topics before we start this section  

1. What is ACI?  AKS?  ACR? 
1. Why use one vs the other?  


## Importing and running Databricks notebooks

Run the following notebooks in order.  You will need to import them, link them to git, and make some changes before actually executing them:

* 02.Bike_Buyer_Ingest.ipynb
* 03a.Bike_Buyer_Build_model.ipynb
* 03b.Bike_Buyer_Build_model_runHistory.ipynb
* 04.Bike_Buyer_Deploy_to_ACI.ipynb
* 05.Bike_Buyer_Deploy_to_AKS_existingImage.ipynb



**Let us know as soon as you don't understand something**

Questions|
--------|
Why would you want to declare your csv schema vs inferring it? |
How do we use kbd shortcuts to add a cell above, delete a cell, and add a cell below? |
What is the definition of `regularization rate`? |
Did we really need to use Databricks for this use case?  What other technologies could've been used?|
What is APIM and why should we use it?  |
What is the default VM size in AKS when you don't specify the size?|







