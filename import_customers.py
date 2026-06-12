import pandas as pd
from sqlalchemy import create_engine

from config.settings import settings

engine = create_engine(settings.DATABASE_URL)

print("Loading dataset...")

df = pd.read_csv("amazon_ecommerce_1M.csv")

customers = df[["user_id", "location", "device", "payment_method"]]

customers = customers.drop_duplicates(subset=["user_id"])

print("Unique customers:", len(customers))

customers.head(1000).to_sql(
    "customers",
    engine,
    if_exists="append",
    index=False,
)

print("1000 customers inserted successfully!")
