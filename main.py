"""
This module contains a CO2 data analysis script.
"""

import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import bar_chart_race as bcr

# Load dataset
df = pd.read_csv("data/owid-co2-data.csv")

# Select relevant columns
cols = ["country", "year", "co2", "co2_per_capita", "population", "iso_code"]
df_small = df[cols].copy()

# Filter years between 1950 and 2000 and keep only real countries (ISO code of length 3)
df_small = df_small[(df_small['year'] >= 1950) & (df_small['year'] < 2000)]
df_small = df_small[df_small['iso_code'].str.len() == 3]

# Compute percentage change in CO2 emissions by country
df_small['diff_pct'] = df_small.groupby('country')['co2'].pct_change() * 100

# Remove meaningless pct_change values when previous CO2 < 1
df_small.loc[df_small.groupby(
    'country')['co2'].shift(1) < 1, 'diff_pct'] = None

# Select top 10 spikes in percentage change
top_diff_countries = df_small.sort_values(
    by="diff_pct", ascending=False).head(10)
top_diff_country_unique = top_diff_countries['country'].unique()

# Compute global CO2 trend
global_trend = (
    df_small.groupby("year")["co2"]
    .sum()
    .reset_index(name="global_co2")
)

# Create a dictionary of trends for the top countries
trends = {
    c: df_small[df_small['country']
                == c].sort_values("year")
    for c in top_diff_country_unique
}

# ----------- VISUALIZATION -----------

fig, ax = plt.subplots()

# Plot CO2 trends of the top 10 countries
for c, df_c in trends.items():
    ax.plot(df_c["year"], df_c["co2"], label=c)

# Highlight top 10 spikes with red points and annotate with country name
for _, row in top_diff_countries.iterrows():
    ax.scatter(row["year"], row["co2"], color="red", zorder=5)
    ax.text(row["year"], row["co2"], row["country"], fontsize=8, rotation=30)

# Labels and title
ax.set_xlabel("Année")
ax.set_ylabel("Émissions de CO₂ (millions de tonnes)")
ax.set_title("Évolution du CO₂ des pays avec les plus fortes variations")
plt.grid(True)
plt.legend()
plt.tight_layout()  # Avoid clipping of labels

plt.show()

# ----------- VISUALIZATION MAP ANIMATION -----------

# df["part_mondiale"] = df["co2"] / \
#     df.groupby("year")["co2"].transform("sum") * 100

# figure = px.choropleth(df,
#                        locations="iso_code",
#                        color="part_mondiale",
#                        hover_data=["country", "co2", "part_mondiale"],
#                        animation_frame="year")
# figure.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# figure.show()

# ----------- VISUALIZATION BAR CHART -----------

# df_race = df.pivot(index="year", columns="country", values="co2")
# df_race = df_race.fillna(0)

# bcr.bar_chart_race(df=df_race,
#                    filename='bar_race.mp4',   # <- crée un fichier vidéo
#                    orientation='h',
#                    sort='desc',
#                    n_bars=10,
#                    steps_per_period=10,
#                    period_length=500
#                    )
