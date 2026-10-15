import pandas as pd

df = pd.read_csv("source.csv")

print("=== CLIENTS SURVEILLÉS ===")

for _, row in df.iterrows():
    print(row["Client"])
