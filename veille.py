import pandas as pd

print("=== VEILLE CULTURELLE ===")

try:
    df = pd.read_csv("sources.csv")
    print(df.head())

except Exception as e:
    print("Erreur :", e)
