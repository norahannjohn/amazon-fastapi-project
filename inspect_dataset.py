import pandas as pd

df = pd.read_csv("amazon_ecommerce_1M.csv")

print("Unique Categories:")
print(df["category"].nunique())

print("\nTop Categories:")
print(df["category"].value_counts().head(10))