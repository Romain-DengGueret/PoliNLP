import polars as pl
import os

# Define the expected file path
MINIMA_SOCIAUX = "trajectoires-des-beneficiaires-de-minima-sociaux"
DATA_PATH = os.path.expanduser(f"~/work/PoliNLP/data/raw/{MINIMA_SOCIAUX}.parquet")


def test_dataframe_is_polars():
    """Test if the loaded DataFrame is a Polars DataFrame."""
    df = pl.read_parquet(DATA_PATH)  # Simulating the behavior in eda.py
    assert isinstance(df, pl.DataFrame), "The loaded object is not a Polars DataFrame"


def test_parquet_file_exists():
    """Test if the expected .parquet file exists in the directory."""
    assert os.path.exists(DATA_PATH), f"Expected parquet file not found: {DATA_PATH}"
