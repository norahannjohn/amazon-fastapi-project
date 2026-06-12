from sqlalchemy.orm import Session

from app.schemas import CustomerCreate

from app.services.customer_service import (
    get_customers_service,
    get_customer_service,
    get_customer_orders_service,
    get_customer_purchases_service,
    create_customer_service,
)


def get_customers_handler(db: Session):
    return get_customers_service(db)


def get_customer_handler(db: Session, user_id: str):

    customer = get_customer_service(db, user_id)

    if not customer:
        raise ValueError("Customer not found")

    return customer


def get_customer_orders_handler(db: Session, user_id: str):

    customer = get_customer_orders_service(db, user_id)

    if not customer:
        raise ValueError("Customer not found")

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


def get_customer_purchases_handler(db: Session, user_id: str):

    customer = get_customer_purchases_service(db, user_id)

    if not customer:
        raise ValueError("Customer not found")

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


def create_customer_handler(db: Session, customer: CustomerCreate):

    create_customer_service(db, customer)

    return {"message": "Customer created successfully"}
