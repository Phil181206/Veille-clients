import pandas as pd

df = pd.read_csv("sources.csv")

print("=== CLIENTS SURVEILLÉS ===")

for _, row in df.iterrows():
    print(row["Client"])
