import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

rapport = []

df = pd.read_csv("sources.csv")

rapport.append("VEILLE CULTURELLE")
rapport.append(f"Date : {datetime.now()}")
rapport.append("")

for _, row in df.iterrows():

    client = row["Client"]

    rapport.append("=" * 50)
    rapport.append(client)

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

            for balise in soup.find_all(
                ["h1", "h2", "h3"]
            ):

                texte = balise.get_text(
                    strip=True
                )

                if len(texte) > 10:
                    titres.append(texte)

            rapport.append("")
            rapport.append(f"{colonne} :")

            for titre in titres[:10]:
                rapport.append(f"- {titre}")

        except Exception as e:

            rapport.append(
                f"Erreur {colonne} : {e}"
            )

    rapport.append("")

texte_final = "\n".join(rapport)

with open(
    "rapport.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(texte_final)

print(texte_final)
