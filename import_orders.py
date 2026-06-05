import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:root123@localhost:5432/amazon_ecommerce_db"

engine = create_engine(DATABASE_URL)

print("Loading dataset...")

df = pd.read_csv("amazon_ecommerce_1M.csv")

# Get first 1000 imported IDs
customer_ids = set(
    pd.read_sql("SELECT user_id FROM customers", engine)["user_id"]
)

product_ids = set(
    pd.read_sql("SELECT product_id FROM products", engine)["product_id"]
)

seller_ids = set(
    pd.read_sql("SELECT seller_id FROM sellers", engine)["seller_id"]
)

orders = df[
    (
        df["user_id"].isin(customer_ids)
    )
    &
    (
        df["product_id"].isin(product_ids)
    )
    &
    (
        df["seller_id"].isin(seller_ids)
    )
]

orders = orders[
    [
        "user_id",
        "product_id",
        "seller_id",
        "purchase_date",
        "shipping_time_days",
        "is_returned",
        "delivery_status"
    ]
]

print("Matching orders found:", len(orders))

orders.head(1000).to_sql(
    "orders",
    engine,
    if_exists="append",
    index=False
)

print("Orders imported successfully!")