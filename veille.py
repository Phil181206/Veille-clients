import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_csv("sources.csv")

print("=== VEILLE CULTURELLE ===")

for _, row in df.iterrows():

    client = row["Client"]

    print(f"\n### {client}")

    for colonne in ["Actualites", "Agenda"]:

        try:

            url = row[colonne]

            if pd.isna(url):
                continue

            page = requests.get(
                url,
                timeout=20,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            soup = BeautifulSoup(
                page.text,
                "html.parser"
            )

            titres = []

            for balise in soup.find_all(["h1", "h2", "h3"]):

                texte = balise.get_text(strip=True)

                if len(texte) > 8:
                    titres.append(texte)

            print(f"\n{colonne}")

            for titre in titres[:10]:
                print("-", titre)

        except Exception as e:
            print("Erreur :", e)
