## Kubeflow 

[kubeflow documentation](https://github.com/kubeflow/kubeflow)

Kubeflow uses ksonnet templates to package and deploy components.  ksonnet simplifies defining an application configuration, updating the configuration over time, and specializing it for different clusters and environments.  

### Ksonnet (not needed anymore?)

Install ksonnet locally on your dev machine.  [Some instructions on installation and validation](https://ksonnet.io/get-started/).  ksonnet is deprecated and hopefully kubeflow will find an alternate way to deploy soon.  ksonnet can be a pain to install locally, here's how I do it from WSL/Ubuntu

_shouldn't be needed anymore_ 
**Skip this**

Sorry for these instructions, kubeflow is changing rapidly.  Leaving these instructions _just in case_.  

```bash
sudo apt-get install golang-go
#go version
export GOPATH=$(go env GOPATH)
PATH=$PATH:$GOPATH/bin

go get github.com/ksonnet/ksonnet

cd $GOPATH/src/github.com/ksonnet/ksonnet
make install
# let's ensure it is working
ks --help
```

### Istio

Now install Istio into your AKS cluster

```bash

ISTIO_VERSION=1.7.3

curl -sL "https://github.com/istio/istio/releases/download/$ISTIO_VERSION/istioctl-$ISTIO_VERSION-linux-amd64.tar.gz" | tar xz
sudo mv ./istioctl /usr/local/bin/istioctl
sudo chmod +x /usr/local/bin/istioctl
istioctl operator init
kubectl get all -n istio-operator
istioctl profile dump default
kubectl create ns istio-system
kubectl apply -f /path_to/Lab102/istio.aks.yaml 
#wait until everything is ready
#kubectl describe pod can help with an y errors as can
#kubectl logs -n istio-operator -l name=istio-operator -f
kubectl get all -n istio-system
```


### Install Kubeflow on AKS and create our kubeflow app

I assume WSL/ubuntu.

Kubeflow is really just a bunch of commands that look a lot like `kubectl` wrapped in a command called `kfctl`.  

Find the release you want to download from here:  https://github.com/kubeflow/kfctl/releases/tag/v1.1.0 then copy the link address to the env var below.

```bash
# vars

# this is what we will call our kubeflow app
export KF_NAME=tfmnist
# see above
SRC_LOC=https://github.com/kubeflow/kfctl/releases/download/v1.1.0/kfctl_v1.1.0-0-g9a3621e_linux.tar.gz
# Set the path to the base directory where you want to store one or more Kubeflow deployments. 
# Then set the Kubeflow application directory for this deployment.
export BASE_DIR="/mnt/c/dave/kubeflow"
export KF_DIR=${BASE_DIR}/${KF_NAME}
# Set the configuration file to use, such as the file specified below:
#export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.1-branch/kfdef/kfctl_azure.v1.1.0.yaml"
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.1-branch/kfdef/kfctl_azure_aad.v1.1.0.yaml"


# download kfctl src
wget $SRC_LOC
tar -xvf kfctl_v1.1.0-0-g9a3621e_linux.tar.gz

export PATH=$PATH:<path to where kfctl was unpacked>

curl -L -o kfctl_azure_aad.v1.1.0.yaml ${CONFIG_URI}

# Generate and deploy Kubeflow:
mkdir -p ${KF_DIR}
cd ${KF_DIR}
kfctl apply -V -f kfctl_azure_aad.v1.1.0.yaml
# this might go into a loop of WARN messages around cert-manager
# look in kf-istio-resources.yaml and change sni_hosts to sniHosts



```