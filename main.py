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

russia_trend = df_small[df_small['country'] == "Russia"].sort_values("year")
china_trend = df_small[df_small['country'] == "China"].sort_values("year")
usa_trend = df_small[df_small['country']
                     == "United States"].sort_values("year")

print("Évolution globale des émissions (quelques lignes) :")
print(global_trend.head(40))

# ----------- VISUALISATION -----------

x = global_trend["year"]
y = global_trend["global_co2"]
xRussia = russia_trend["year"]
yRussia = russia_trend["co2"]
xChina = china_trend["year"]
yChina = china_trend["co2"]
xUsa = usa_trend["year"]
yUsa = usa_trend["co2"]

fig, ax = plt.subplots()
ax.plot(x, y, label="global")
ax.plot(xRussia, yRussia, label="Russia")
ax.plot(xChina, yChina, label="China")
ax.plot(xUsa, yUsa, label="USA")

plt.xlabel("Année")
plt.ylabel("Émissions de CO₂ (millions de tonnes)")
plt.grid(True)
plt.legend()

plt.show()
