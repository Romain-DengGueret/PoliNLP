import polars as pl

minimasociaux = "trajectoires-des-beneficiaires-de-minima-sociaux"
df_eda = pl.read_parquet("~/work/PoliNLP/data/raw/{}.parquet".format(minimasociaux))

# Checking for null values
print(
    "NaN : ", df_eda.select(pl.any_horizontal(pl.all().is_null().any())).item()
)  # No NaN

# Checking for duplicates
print("Duplicates : ", df_eda.is_duplicated().sum())  # No duplicates
