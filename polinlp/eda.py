import polars as pl

minimasociaux = "trajectoires-des-beneficiaires-de-minima-sociaux"
df_eda = pl.read_parquet("~/work/PoliNLP/data/{}.parquet".format(minimasociaux))

df_eda.head()
