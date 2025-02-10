import os
import requests  # type: ignore
import polars as pl

# Defining endpoint
drees = "https://data.drees.solidarites-sante.gouv.fr/api/explore/v2.1"
datasets = "/catalog/datasets/"
minimasociaux = "trajectoires-des-beneficiaires-de-minima-sociaux"
jsonexport = "/exports/json"

url = drees + datasets + minimasociaux + jsonexport


# Function to connect to api
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

# Ensure the output directory exists
output_dir = "~/work/PoliNLP/data/raw/"
os.makedirs(
    os.path.expanduser(output_dir), exist_ok=True
)  # Create directory if it doesn't exist

# Export parquet
df_etl.write_parquet(os.path.expanduser(f"{output_dir}{minimasociaux}.parquet"))
