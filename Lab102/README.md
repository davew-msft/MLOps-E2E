## Kubeflow 

[kubeflow documentation](https://github.com/kubeflow/kubeflow)

Kubeflow uses ksonnet templates to package and deploy components.  ksonnet simplifies defining an application configuration, updating the configuration over time, and specializing it for different clusters and environments.  

1. Install ksonnet locally on your dev machine.  [Some instructions on installation and validation](https://ksonnet.io/get-started/).  ksonnet is deprecated and hopefully kubeflow will find an alternate way to deploy soon.  ksonnet can be a pain to install locally, here's how I do it from WSL/Ubuntu

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

I assume WSL/ubuntu

```bash
# vars
# where you want to put the kubeflow source code and the version of kubeflow you want to use
KUBEFLOW_SRC="/mnt/c/dave/kubeflow"
# this is what we will call our kubeflow app
KFAPP=tfmnist
export KUBEFLOW_TAG=v0.4.1

mkdir ${KUBEFLOW_SRC}
cd ${KUBEFLOW_SRC}

curl https://raw.githubusercontent.com/kubeflow/kubeflow/${KUBEFLOW_TAG}/scripts/download.sh | bash


# Initialize a kubeflow app
${KUBEFLOW_SRC}/scripts/kfctl.sh init ${KFAPP} --platform none

# Generate kubeflow app
cd ${KFAPP}
${KUBEFLOW_SRC}/scripts/kfctl.sh generate k8s

# Deploy Kubeflow app
${KUBEFLOW_SRC}/scripts/kfctl.sh apply k8s
```