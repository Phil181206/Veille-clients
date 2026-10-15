import pandas as pd

print("Veille culturelle démarrée")

try:
    df = pd.read_csv("sources.csv")
    print(df.head())
except Exception as e:
    print(e)
