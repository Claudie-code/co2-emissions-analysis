import pandas as pd
df = pd.read_csv("data/owid-co2-data.csv")

cols = ["country", "year", "co2", "co2_per_capita", "population"]
df_small = df[cols].copy()

print("Aperçu du DataFrame simplifié :")
print(df_small.head(), "\n")

global_trend = (
    df_small.groupby("year")["co2"]
    .sum()
    .reset_index(name="global_co2")
)

print("Évolution globale des émissions (quelques lignes) :")
print(global_trend.head(20))
