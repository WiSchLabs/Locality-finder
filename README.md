<p align="center">
  <img src="https://raw.githubusercontent.com/WiSchLabs/Locality-finder/master/main/static/main/img/locality-finder.png" width="325px">
</p>

# [Locality Finder](https://locality-finder-helm.sh4ke.rocks/)
[![](https://images.microbadger.com/badges/version/wischlabs/locality_finder.svg)](https://microbadger.com/images/wischlabs/locality_finder "Get your own version badge on microbadger.com")
[![](https://images.microbadger.com/badges/image/wischlabs/locality_finder.svg)](https://microbadger.com/images/wischlabs/locality_finder "Get your own image badge on microbadger.com")

The locality finder is a Django Web-Application, which let's you find local events in your neighboorhood.

## Installation

1. Docker-Compose 
```
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input
```

Afterwards you can browse to http://127.0.0.1:8080/ and see your brand new locality finder instance.

2. Kubernetes

We also deliver a Helm chart to easily deploy this application into a Kubernetes Cluster.
Simply copy the `helm_chart/prod_values.example.yaml` to `helm_chart/prod_values.yaml` and fill it out with your production values.

Afterwards you can start your new Helm release like so:
```
helm install -f helm_chart/prod_values.yaml --namespace <a_new_namespace> helm_chart
```

There are a few Requirements, though.
1. You need top already have setup Helm / Tiller into your Kubernetes cluster.
2. This also includes a ServiceAccount and ClusterRoleBinding with appropriate rights.
3. You need a working Issuer or ClusterIssuer to obtain a valid let's-encrypt certificate. It does not matter, which Ingress-Controller you are installing into your Cluster as long as it promotes a working Issuer. Here are some examples for issuers:
    * https://github.com/jetstack/cert-manager
    * https://github.com/janeczku/rancher-letsencrypt
    
    
3. Locally
This option is __not__ recommended, because you need to have a running PostGIS installation on your server.
If you still want to run it locally, simply install all requirements into your system or a python virtual environment and point your django settings to `settings/base_settings`. You still need to adapt your database settings though.

Your workflow might look like this:
```
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
pip install -r docker_requirements.txt

DJANGO_SETTINGS_MODULE=settings.base_settings
python manage.py runserver 0.0.0.0:8080
python manage.py migrate
```
