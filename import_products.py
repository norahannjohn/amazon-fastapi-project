import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:root123@localhost:5432/amazon_ecommerce_db"

engine = create_engine(DATABASE_URL)

print("Loading dataset...")

df = pd.read_csv("amazon_ecommerce_1M.csv")

products = df[
    [
        "product_id",
        "category",
        "subcategory",
        "brand",
        "price",
        "discount",
        "final_price",
        "rating",
        "review_count",
        "stock"
    ]
]

products = products.drop_duplicates(subset=["product_id"])

print("Unique products:", len(products))

products.head(1000).to_sql(
    "products",
    engine,
    if_exists="append",
    index=False
)

print("1000 products inserted successfully!")