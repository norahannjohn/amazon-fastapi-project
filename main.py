from fastapi import FastAPI, HTTPException, status


from database import SessionLocal
from schemas import CustomerCreate, OrderCreate, ProductCreate, SellerCreate
from models import Customer, Product, Seller, Order

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Amazon E-commerce API is running"}


@app.get("/customers")
def get_customers():

    db = SessionLocal()

    try:

        customers = db.query(Customer).limit(10).all()

        result = []

        for customer in customers:
            result.append(
                {
                    "user_id": customer.user_id,
                    "location": customer.location,
                    "device": customer.device,
                    "payment_method": customer.payment_method,
                }
            )

        return result

    except Exception:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.get("/products")
def get_products():

    db = SessionLocal()

    try:

        products = db.query(Product).limit(10).all()

        result = []

        for row in products:
            result.append(
                {
                    "product_id": row.product_id,
                    "category": row.category,
                    "subcategory": row.subcategory,
                    "brand": row.brand,
                    "price": row.price,
                    "discount": row.discount,
                    "final_price": row.final_price,
                    "rating": row.rating,
                    "review_count": row.review_count,
                    "stock": row.stock,
                }
            )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:
        db.close()


@app.get("/customers/{user_id}")
def get_customer(user_id: str):

    db = SessionLocal()

    try:
        customer = db.query(Customer).filter(Customer.user_id == user_id).first()
        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found",
            )

        return {
            "user_id": customer.user_id,
            "location": customer.location,
            "device": customer.device,
            "payment_method": customer.payment_method,
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.get("/customers/{user_id}/orders")
def get_customer_orders(user_id: str):

    db = SessionLocal()

    try:

        customer = db.query(Customer).filter(Customer.user_id == user_id).first()

        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found",
            )

        result = []

        for order in customer.orders:
            result.append(
                {
                    "order_id": order.order_id,
                    "user_id": order.user_id,
                    "product_id": order.product_id,
                    "seller_id": order.seller_id,
                    "purchase_date": str(order.purchase_date),
                    "shipping_time_days": order.shipping_time_days,
                    "is_returned": order.is_returned,
                    "delivery_status": order.delivery_status,
                }
            )

        return result

    except HTTPException:
        raise

    except Exception:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.get("/customers/{user_id}/purchases")
def get_customer_purchases(user_id: str):

    db = SessionLocal()

    try:

        customer = db.query(Customer).filter(Customer.user_id == user_id).first()

        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found",
            )

        result = []

        for order in customer.orders:
            result.append(
                {
                    "order_id": order.order_id,
                    "purchase_date": str(order.purchase_date),
                    "delivery_status": order.delivery_status,
                    "product_id": order.product.product_id,
                    "brand": order.product.brand,
                    "category": order.product.category,
                    "final_price": order.product.final_price,
                    "rating": order.product.rating,
                }
            )

        return result

    except HTTPException:
        raise

    except Exception:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.get("/sellers")
def get_sellers():

    db = SessionLocal()

    try:

        sellers = db.query(Seller).limit(10).all()

        result = []

        for seller in sellers:
            result.append(
                {
                    "seller_id": seller.seller_id,
                    "seller_rating": seller.seller_rating,
                }
            )

        return result

    except Exception:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.get("/sellers/{seller_id}")
def get_seller(seller_id: str):

    db = SessionLocal()

    try:

        seller = db.query(Seller).filter(Seller.seller_id == seller_id).first()

        if not seller:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Seller not found",
            )

        return {
            "seller_id": seller.seller_id,
            "seller_rating": seller.seller_rating,
        }

    except HTTPException:
        raise

    except Exception:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.get("/products/{product_id}")
def get_product(product_id: str):

    db = SessionLocal()

    try:

        product = db.query(Product).filter(Product.product_id == product_id).first()

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

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
            "stock": product.stock,
        }

    except HTTPException:
        raise

    except Exception:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.get("/orders")
def get_orders():

    db = SessionLocal()

    try:

        orders = db.query(Order).limit(10).all()

        result = []

        for order in orders:
            result.append(
                {
                    "order_id": order.order_id,
                    "user_id": order.user_id,
                    "product_id": order.product_id,
                    "seller_id": order.seller_id,
                    "purchase_date": order.purchase_date,
                    "shipping_time_days": order.shipping_time_days,
                    "is_returned": order.is_returned,
                    "delivery_status": order.delivery_status,
                }
            )

        return result

    except Exception:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.get("/orders/{order_id}")
def get_order(order_id: int):

    db = SessionLocal()

    try:

        order = db.query(Order).filter(Order.order_id == order_id).first()

        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found",
            )

        return {
            "order_id": order.order_id,
            "user_id": order.user_id,
            "product_id": order.product_id,
            "seller_id": order.seller_id,
            "purchase_date": order.purchase_date,
            "shipping_time_days": order.shipping_time_days,
            "is_returned": order.is_returned,
            "delivery_status": order.delivery_status,
        }

    except HTTPException:
        raise

    except Exception:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.post("/customers", status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate):

    db = SessionLocal()

    try:

        new_customer = Customer(
            user_id=customer.user_id,
            location=customer.location,
            device=customer.device,
            payment_method=customer.payment_method,
        )

        db.add(new_customer)

        db.commit()

        return {"message": "Customer created successfully"}

    except HTTPException:
        raise

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.post(
    "/orders",
    status_code=status.HTTP_201_CREATED,
)
def create_order(order: OrderCreate):

    db = SessionLocal()

    try:

        new_order = Order(
            user_id=order.user_id,
            product_id=order.product_id,
            seller_id=order.seller_id,
            purchase_date=order.purchase_date,
            shipping_time_days=order.shipping_time_days,
            is_returned=order.is_returned,
            delivery_status=order.delivery_status,
        )

        db.add(new_order)

        db.commit()

        return {"message": "Order created successfully"}

    except HTTPException:
        raise

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.post(
    "/products",
    status_code=status.HTTP_201_CREATED,
)
def create_product(product: ProductCreate):

    db = SessionLocal()

    try:

        new_product = Product(
            product_id=product.product_id,
            category=product.category,
            subcategory=product.subcategory,
            brand=product.brand,
            price=product.price,
            discount=product.discount,
            final_price=product.final_price,
            rating=product.rating,
            review_count=product.review_count,
            stock=product.stock,
        )

        db.add(new_product)

        db.commit()

        return {"message": "Product created successfully"}

    except HTTPException:
        raise

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@app.post(
    "/sellers",
    status_code=status.HTTP_201_CREATED,
)
def create_seller(seller: SellerCreate):

    db = SessionLocal()

    try:

        new_seller = Seller(
            seller_id=seller.seller_id,
            seller_rating=seller.seller_rating,
        )

        db.add(new_seller)

        db.commit()

        return {"message": "Seller created successfully"}

    except HTTPException:
        raise

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()
