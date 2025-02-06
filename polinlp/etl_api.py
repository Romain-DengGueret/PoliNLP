import requests  # type: ignore
import polars as pl
import os

# Remonter d'un niveau
parent_dir = os.getcwd() + "/PoliNLP"

# Construire les chemins dynamiques
data_path = parent_dir + "/data"
prepro_data_path = data_path + "/prepro"

# Defining endpoint
drees = "https://data.drees.solidarites-sante.gouv.fr/api/explore/v2.1"
datasets = "/catalog/datasets/"
minimasociaux = "/trajectoires-des-beneficiaires-de-minima-sociaux/exports/json"

endpoint = drees + datasets + minimasociaux

# Requests
response = requests.get(endpoint).json()  # We get a json file

# Convert all in str
cleaned_response = [
    {
        key: str(value) if not isinstance(value, (int, float)) else value
        for key, value in entry.items()
    }
    for entry in response
]

# Results in a Polars DataFrame
df = pl.DataFrame(cleaned_response)

# Writing parquet
path = prepro_data_path + "/trajectoires_beneficiares_minimas_sociaux.parquet"
df.write_parquet(path)
