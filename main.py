"""
Ce module contient un script d'analyse des données CO2.
"""

import matplotlib.pyplot as plt
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

countries = ["Russia", "China", "United States"]
trends = {
    c: df_small[df_small['country'] == c].sort_values("year") for c in countries
}

print("Évolution globale des émissions (quelques lignes) :")
print(global_trend.head(40))
print("trends", trends)

# ----------- VISUALISATION -----------

fig, ax = plt.subplots()
ax.plot(global_trend["year"], global_trend["global_co2"], label="Global")
for c, df_c in trends.items():
    ax.plot(df_c["year"], df_c["co2"], label=c)

plt.xlabel("Année")
plt.ylabel("Émissions de CO₂ (millions de tonnes)")
plt.grid(True)
plt.legend()

plt.show()
