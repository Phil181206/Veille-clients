import pandas as pd
import requests
from bs4 import BeautifulSoup

print("=== VEILLE CULTURELLE ===")

try:
    df = pd.read_csv("sources.csv")

    for index, row in df.iterrows():

        client = row["Client"]

        print("\n----------------")
        print(client)

        for colonne in ["Actualites", "Agenda"]:

            url = row[colonne]

            if pd.isna(url):
                continue

            try:

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

                titres
