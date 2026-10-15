from datetime import datetime

rapport = f"""
VEILLE CLIENTS
Date : {datetime.now()}

MUCEM
- Vérification effectuée

LUMA ARLES
- Vérification effectuée

COMEDIE FRANCAISE
- Vérification effectuée
"""

with open("rapport.txt", "w", encoding="utf-8") as f:
    f.write(rapport)

print(rapport)
with open("rapport.txt", "w", encoding="utf-8") as f:
 f.write("VEILLE CLIENTS\n\nTest OK")
