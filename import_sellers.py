import pandas as pd
from sqlalchemy import create_engine

from config.settings import settings

engine = create_engine(settings.DATABASE_URL)

print("Loading dataset...")

df = pd.read_csv("amazon_ecommerce_1M.csv")

sellers = df[["seller_id", "seller_rating"]]

sellers = sellers.drop_duplicates(subset=["seller_id"])

print("Unique sellers:", len(sellers))

sellers.head(1000).to_sql("sellers", engine, if_exists="append", index=False)

print("1000 sellers inserted successfully!")
