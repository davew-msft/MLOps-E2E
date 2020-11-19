## Simplified MLOps Solution

  * We deploy a simple model quickly and don't worry about the implementation details of model development
  * we do focus on 
    * how `score.py` works
    * how to build a conda env that will work with azdo
  * we build up the azdo pipelines and focus there on how to do the automation
  * the focus of this lab is simply to understand the patterns for the azdo pipelines

## Get a model ready

Let's quickly get an employee attrition model working.  

* In your AMLS compute (or local dev env if desired) open `Lab401/attrition-model.ipynb` and follow instructions


## Let's do MLOps

### Import this repo

Go to your Azure DevOps project, into the Repos area.
Click on the Git repo dropdown at the top of the page and then on "Import Repository".

Under clone URL: `github.com/davew-msft/MLOps-E2E.git`