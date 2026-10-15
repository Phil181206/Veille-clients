import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

SOURCE_FILE = "sources.csv"
HISTORIQUE_FILE = "historique.csv"

# Lecture des sources
df = pd.read_csv(SOURCE_FILE)

nouveaux = []
actuels = []

# Lecture historique précédent
if os.path.exists(HISTORIQUE_FILE):
    historique = pd.read_csv(HISTORIQUE_FILE)
else:
    historique = pd.DataFrame(columns=["Client", "Titre"])

for _, row in df.iterrows():

    client = row["Client"]

    for colonne in ["Actualites", "Agenda"]:

        try:

            url = row[colonne]

            if pd.isna(url):
                continue

            page = requests.get(
                url,
                timeout=20,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            soup = BeautifulSoup(page.text, "html.parser")

            titres = []

            for balise in soup.find_all(["h1", "h2", "h3"]):

                texte = balise.get_text(strip=True)

                if len(texte) > 10:
                    titres.append(texte)

            titres = titres[:10]

            for titre in titres:

                actuels.append([client, titre])

                deja_vu = (
                    (
                        historique["Client"] == client
                    )
                    &
                    (
                        historique["Titre"] == titre
                    )
                ).any()

                if not deja_vu:
                    nouveaux.append([client, titre])

        except Exception as e:
            print(f"Erreur {client} : {e}")

# Sauvegarde historique
pd.DataFrame(
    actuels,
    columns=["Client", "Titre"]
).to_csv(
    HISTORIQUE_FILE,
    index=False
)

# Rapport
rapport = []
rapport.append("VEILLE HEBDOMADAIRE")
rapport.append(f"Date : {datetime.now()}")
rapport.append("")

for client, titre in nouveaux:
    rapport.append(f"{client} : {titre}")

texte = "\n".join(rapport)

with open(
    "rapport.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(texte)

print(texte)
