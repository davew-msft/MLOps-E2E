## Lab 10:  Setup

* Do Lab 1 if you have not done that yet.  
### Discussion topics before we start this section  

* There are different tools we can use for python/jupyter development including:
  * **Best Approach**:  spin up a compute instance in AMLS and use that for development
    * compute instances have a built-in JupyterLab server that can be shared among the team
    * you can use vscode as the IDE and use Remote development in vscode using ssh
  * pretty much anything else that supports python and can call an API (basically, python) should work including everything from pyCharm to vim and emacs.  

## Setup

1. Make sure you have an Azure DevOps (AzDO) subscription **or** a github account.
1. Clone this repo into AzDO/gh
2. Make sure you have an AMLS workspace.  
1. decide which Jupyter/python development tool you want to use (suggestion:  AMLS compute)
1. clone this git repo into your Juyter/python environment:  `https://github.com/davew-msft/MLOps-E2E`

>In the real world you would want to use your own gh repo.  Why?  You may notice a `Terminal` option in Azure Notebooks.  That option allows you to `git pull` and `git push` to gh.  

Play around with the Jupyter environment by examining some of the .ipynb files.    



