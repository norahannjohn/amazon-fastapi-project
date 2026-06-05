from fastapi import FastAPI
from sqlalchemy import text

from database import SessionLocal
from schemas import CustomerCreate, OrderCreate, ProductCreate, SellerCreate

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
@app.get("/sellers")
def get_sellers():

    db = SessionLocal()

    sellers = db.execute(
        text("""
            SELECT *
            FROM sellers
            LIMIT 10
        """)
    )

    result = []

    for row in sellers:
        result.append({
            "seller_id": row.seller_id,
            "seller_rating": row.seller_rating
        })

    db.close()

    return result
@app.get("/sellers/{seller_id}")
def get_seller(seller_id: str):

    db = SessionLocal()

    seller = db.execute(
        text("""
            SELECT *
            FROM sellers
            WHERE seller_id = :seller_id
        """),
        {"seller_id": seller_id}
    ).fetchone()

    db.close()

    if not seller:
        return {"message": "Seller not found"}

    return {
        "seller_id": seller.seller_id,
        "seller_rating": seller.seller_rating
    }
@app.get("/products/{product_id}")
def get_product(product_id: str):

    db = SessionLocal()

    product = db.execute(
        text("""
            SELECT *
            FROM products
            WHERE product_id = :product_id
        """),
        {"product_id": product_id}
    ).fetchone()

    db.close()

    if not product:
        return {"message": "Product not found"}

    return {
        "product_id": product.product_id,
        "category": product.category,
        "subcategory": product.subcategory,
        "brand": product.brand,
        "price": product.price,
        "discount": product.discount,
        "final_price": product.final_price,
        "rating": product.rating,
        "review_count": product.review_count,
        "stock": product.stock
    }
@app.get("/orders")
def get_orders():

    db = SessionLocal()

    orders = db.execute(
        text("""
            SELECT *
            FROM orders
            LIMIT 10
        """)
    )

    result = []

    for row in orders:
        result.append({
            "order_id": row.order_id,
            "user_id": row.user_id,
            "product_id": row.product_id,
            "seller_id": row.seller_id,
            "purchase_date": row.purchase_date,
            "shipping_time_days": row.shipping_time_days,
            "is_returned": row.is_returned,
            "delivery_status": row.delivery_status
        })

    db.close()

    return result
@app.get("/orders/{order_id}")
def get_order(order_id: int):

    db = SessionLocal()

    order = db.execute(
        text("""
            SELECT *
            FROM orders
            WHERE order_id = :order_id
        """),
        {"order_id": order_id}
    ).fetchone()

    db.close()

    if not order:
        return {"message": "Order not found"}

    return {
        "order_id": order.order_id,
        "user_id": order.user_id,
        "product_id": order.product_id,
        "seller_id": order.seller_id,
        "purchase_date": order.purchase_date,
        "shipping_time_days": order.shipping_time_days,
        "is_returned": order.is_returned,
        "delivery_status": order.delivery_status
    }

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

@app.post("/orders")
def create_order(order: OrderCreate):

    db = SessionLocal()

    db.execute(
        text("""
            INSERT INTO orders
            (
                user_id,
                product_id,
                seller_id,
                purchase_date,
                shipping_time_days,
                is_returned,
                delivery_status
            )

            VALUES
            (
                :user_id,
                :product_id,
                :seller_id,
                :purchase_date,
                :shipping_time_days,
                :is_returned,
                :delivery_status
            )
        """),
        {
            "user_id": order.user_id,
            "product_id": order.product_id,
            "seller_id": order.seller_id,
            "purchase_date": order.purchase_date,
            "shipping_time_days": order.shipping_time_days,
            "is_returned": order.is_returned,
            "delivery_status": order.delivery_status
        }
    )

    db.commit()

    db.close()

    return {
        "message": "Order created successfully"
    }

@app.post("/products")
def create_product(product: ProductCreate):

    db = SessionLocal()

    db.execute(
        text("""
            INSERT INTO products
            (
                product_id,
                category,
                subcategory,
                brand,
                price,
                discount,
                final_price,
                rating,
                review_count,
                stock
            )

            VALUES
            (
                :product_id,
                :category,
                :subcategory,
                :brand,
                :price,
                :discount,
                :final_price,
                :rating,
                :review_count,
                :stock
            )
        """),
        {
            "product_id": product.product_id,
            "category": product.category,
            "subcategory": product.subcategory,
            "brand": product.brand,
            "price": product.price,
            "discount": product.discount,
            "final_price": product.final_price,
            "rating": product.rating,
            "review_count": product.review_count,
            "stock": product.stock
        }
    )

    db.commit()

    db.close()

    return {
        "message": "Product created successfully"
    }
@app.post("/sellers")
def create_seller(seller: SellerCreate):

    db = SessionLocal()

    db.execute(
        text("""
            INSERT INTO sellers
            (
                seller_id,
                seller_rating
            )

            VALUES
            (
                :seller_id,
                :seller_rating
            )
        """),
        {
            "seller_id": seller.seller_id,
            "seller_rating": seller.seller_rating
        }
    )

    db.commit()

    db.close()

    return {
        "message": "Seller created successfully"
    }