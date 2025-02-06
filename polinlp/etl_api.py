import requests  # type: ignore

# Defining endpoint
drees = "https://data.drees.solidarites-sante.gouv.fr/api/explore/v2.1"
datasets = "/catalog/datasets/"
minimasociaux = "/trajectoires-des-beneficiaires-de-minima-sociaux/exports/json"

endpoint = drees + datasets + minimasociaux

# Requests
response = requests.get(endpoint).json()  # We get a json file
