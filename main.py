import pandas as pd
URL = "https://github.com/owid/co2-data/raw/master/owid-co2-data.csv"
df = pd.read_csv(URL, index_col=0, parse_dates=[0])

print(df.head(5))
