# This is the scenario where the Data Scientist is using Anaconda and Jupyter Notebooks

![Original Data Scientist Work](https://raw.githubusercontent.com/DataSnowman/MLonBigData/master/images/originalDataScientistWork.png)

## Prerequisites

To run the Bike Buyer Model notebook you will need:

1) [Download](https://www.anaconda.com/download/) and install the Anaconda Distribution for you OS
2) Clone this GitHub repository using Git and the following commands: 

    ```sh
    git clone https://github.com/DataSnowman/MLonBigData.git
    ```

### Create an isolated Python environment 

Open a command-line window. Then create a new conda environment named `myenv` (you can choose a different name) with Python 3.6

```sh
conda create -n myenv -y Python=3.6
```
List the conda environments

```sh
conda env list
  ```

Activate the environment.

  ```sh
  conda activate myenv
  ```

Navigate to the correct directory where the `Bike Buyer Maodel.ipynb` file is located

```sh
MLonBigData\BikeBuyer\OriginalDataScientistWork
```

Launch Jupyter Notebooks

  ```sh
  jupyter notebook
  ```


## You can install the Azure Machine Learning service SDK

This takes you to detail on how to [Install the AML SDK](https://docs.microsoft.com/en-us/azure/machine-learning/service/quickstart-create-workspace-with-python#install-the-sdk-1)