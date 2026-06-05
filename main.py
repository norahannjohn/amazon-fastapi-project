from fastapi import FastAPI
from sqlalchemy import text

from database import SessionLocal
from schemas import CustomerCreate

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Amazon E-commerce API is running"}


@app.get("/customers")
def get_customers():

    db = SessionLocal()

    customers = db.execute(
        text("""
            SELECT *
            FROM customers
            LIMIT 10
        """)
    )

    result = []

    for row in customers:
        result.append({
            "user_id": row.user_id,
            "location": row.location,
            "device": row.device,
            "payment_method": row.payment_method
        })

    db.close()

    return result

@app.get("/products")
def get_products():

    db = SessionLocal()

    products = db.execute(
        text("""
            SELECT *
            FROM products
            LIMIT 10
        """)
    )

    result = []

    for row in products:
        result.append({
            "product_id": row.product_id,
            "category": row.category,
            "subcategory": row.subcategory,
            "brand": row.brand,
            "price": row.price,
            "discount": row.discount,
            "final_price": row.final_price,
            "rating": row.rating,
            "review_count": row.review_count,
            "stock": row.stock
        })

    db.close()

    return result

@app.get("/customers/{user_id}")
def get_customer(user_id: str):

    db = SessionLocal()

    customer = db.execute(
        text("""
            SELECT *
            FROM customers
            WHERE user_id = :user_id
        """),
        {"user_id": user_id}
    ).fetchone()

    db.close()

    if not customer:
        return {"message": "Customer not found"}

    return {
        "user_id": customer.user_id,
        "location": customer.location,
        "device": customer.device,
        "payment_method": customer.payment_method
    }

@app.get("/customers/{user_id}/orders")
def get_customer_orders(user_id: str):

    db = SessionLocal()

    orders = db.execute(
        text("""
            SELECT *
            FROM orders
            WHERE user_id = :user_id
        """),
        {"user_id": user_id}
    )

    result = []

    for row in orders:
        result.append({
            "order_id": row.order_id,
            "user_id": row.user_id,
            "product_id": row.product_id,
            "seller_id": row.seller_id,
            "purchase_date": str(row.purchase_date),
            "shipping_time_days": row.shipping_time_days,
            "is_returned": row.is_returned,
            "delivery_status": row.delivery_status
        })

    db.close()

    return result

@app.get("/customers/{user_id}/purchases")
def get_customer_purchases(user_id: str):

    db = SessionLocal()

    purchases = db.execute(
        text("""
            SELECT
                o.order_id,
                o.purchase_date,
                o.delivery_status,

                p.product_id,
                p.brand,
                p.category,
                p.final_price,
                p.rating

            FROM orders o

            JOIN products p
            ON o.product_id = p.product_id

            WHERE o.user_id = :user_id
        """),
        {"user_id": user_id}
    )

    result = []

    for row in purchases:
        result.append({
            "order_id": row.order_id,
            "purchase_date": str(row.purchase_date),
            "delivery_status": row.delivery_status,

            "product_id": row.product_id,
            "brand": row.brand,
            "category": row.category,
            "final_price": row.final_price,
            "rating": row.rating
        })

    db.close()

    return result

@app.post("/customers")
def create_customer(customer: CustomerCreate):

    db = SessionLocal()

    db.execute(
        text("""
            INSERT INTO customers
            (user_id, location, device, payment_method)

            VALUES
            (:user_id, :location, :device, :payment_method)
        """),
        {
            "user_id": customer.user_id,
            "location": customer.location,
            "device": customer.device,
            "payment_method": customer.payment_method
        }
    )

    db.commit()

    db.close()

    return {
        "message": "Customer created successfully"
    }