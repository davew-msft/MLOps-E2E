## Kubeflow 

### Why kubeflow?

Kubernetes solves a lot of thorny data science problems:
* training is parallelizable
* distributed training can be distributed (we'll do that with TensorFlow)

Training at scale:  
<a href="https://www.youtube.com/watch?v=v4N3Krzb8Eg">![OpenAI](./thumbnail.png)</a>

### Prerquisites on your local dev machine

* docker
* az cli
* kubectl
* git
* helm
* ksonnet

### Install AKS

We are going to create a GPU-enabled AKS cluster.  **Make sure you shut this down when you are done to control costs.**

If you already have a GPU enabled AKS cluster then you can skip this step.  

```bash
# change your env vars as needed
SUBSCRIPTION='davew demo'
RES_GROUP=MLOpsWorkshop
LOCATION="eastus"
NODE_SIZE_GPU=Standard_NC6
NODE_SIZE_CPU=Standard_D2_v2
AKS_NAME="davew-aks-gpu" 
NODE_COUNT=3 #number of AKS VMs

az login
az account set --subscription "${SUBSCRIPTION}"
az group create --name $RES_GROUP --location $LOCATION

# determine AKS available versions, then set the most recent
az aks get-versions --location $LOCATION -o table
AKS_VER=1.18.8 


az aks create \
    --node-vm-size $NODE_SIZE_GPU \
    --resource-group $RES_GROUP \
    --name $AKS_NAME \
    --node-count $NODE_COUNT \
    --kubernetes-version $AKS_VER \
    --location $LOCATION \
    --generate-ssh-keys

# this will probably take a while
# now, get the credentials to connect to the AKS cluster.  All this is really is the entry for the kubeconfig file

az aks get-credentials --name $AKS_NAME --resource-group $RES_GROUP

# make sure we are pointing to the correct context
kubectl config get-contexts
kubectl config set-context $AKS_NAME

#For AKS we need to install the NVIDIA Device Plugin (actually, this step should not be needed anymore)

#let's validate
kubectl get nodes
#this should indicate GPU
kubectl describe node <any node name> | grep nvidia.com/gpu
# if not then we need to fix it by installing the daemonset
kubectl create namespace gpu-resources
kubectl apply -f path/to/Lab100/nvidia-device-plugin-ds.yaml
#now doublecheck
kubectl describe node <any node name> | grep nvidia.com/gpu



# don't close your bash shell, we'll use it for the next lab
```

**don't close your bash shell, we'll use it for the next lab**