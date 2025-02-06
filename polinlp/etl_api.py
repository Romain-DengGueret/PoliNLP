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

url = drees + datasets + minimasociaux


def etl_json_to_polarsdf(endpoint: str) -> pl.DataFrame:
    """
    Performs an HTTP GET request on the given endpoint, retrieves the JSON
    data and transforms it into a Polars DataFrame with its own format.

    Args:
        endpoint (str): API URL returning a JSON.

    Returns:
        pl.DataFrame: Polars DataFrame containing the transformed data.
    """

    # Get request
    response = requests.get(endpoint).json()

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

    return df


df_etl = etl_json_to_polarsdf(endpoint=url)

# Writing parquet
path = prepro_data_path + "/trajectoires_beneficiares_minimas_sociaux.parquet"
df_etl.write_parquet(path)
