from pathlib import Path
import requests

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

URL = "https://github.com/owid/co2-data/raw/master/owid-co2-data.csv"
DEST = DATA_DIR / "owid-co2-data.csv"

print(f"Téléchargement des données depuis {URL} ...")

response = requests.get(URL)
response.raise_for_status()  # stoppe si erreur (404, 500…)

with open(DEST, "wb") as f:
    f.write(response.content)

print(f"✅ Données sauvegardées dans {DEST}")
