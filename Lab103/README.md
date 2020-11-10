## JupyterHub on AKS/Kubeflow

[JupyterHub](https://jupyterhub.readthedocs.io/en/latest/) is a multi-user Hub that spawns, manages, and proxies multiple instances of the single-user Jupyter notebook server (JupyterLab). JupyterHub can be used to serve notebooks to a class of students, a corporate data science group, or a scientific research group. Let's look at how we can create JupyterHub to spawn multiple instances of Jupyter Notebook on AKS using Kubeflow.

For familiarity, let's use the tf docker container locally, which has Jupyter notebooks available on it

```bash
docker run -d -p 8888:8888 jupyter/tensorflow-notebook
# the output will be your container id
# we need to use that here to get the URL for jupyter, the first few characters of the id are enough
docker exec 139891b235f jupyter notebook list
# that should give you a URL like this:
#http://0.0.0.0:8888/?token=73e2ed91d737edcc4f9ef1f5f2b77fee82705251da96146f
# you may have to change 0.0.0.0 to localhost

```

Feel free to experiment.  We want a similar, but scalable to a team, solution on AKS.  Let's look at that using Kubeflow.  kubeflow-core already has JupyterHub available.  

```bash
NAMESPACE=kubeflow
kubectl get svc -n=${NAMESPACE}
# you should see entries for jupyter

#let's connect to kubeflow dashboard using a proxy
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
```

Now browse to `http://localhost:8080`, this is kubeflow dashboard.  Take a minute to familiarize yourself with it.  

You should now be able to connect.  