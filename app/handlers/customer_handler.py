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
    """Retrieve all customers.

    Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of customer objects.
    """
    return get_customers_service(db)


def get_customer_handler(db: Session, user_id: str):
    """Retrieve a customer by user ID.

    Args:
        db (Session): Active SQLAlchemy database session.
        user_id (str):Unique identifier of the customer.

    Raises:
        ValueError: If the customer is not found.

    Returns:
        Customer: Customer object.
    """

    customer = get_customer_service(db, user_id)

    if not customer:
        raise ValueError("Customer not found")

    return customer


def get_customer_orders_handler(db: Session, user_id: str):
    """Retrieve all orders placed by a customer.

    Args:
        db (Session): Active SQLAlchemy database session.
        user_id (str):Unique identifier of the customer.

    Raises:
        ValueError: If the customer is not found.

    Returns:
       list: List of customer order details.
    """

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
    """Retrieve a customer's purchase history.

    Args:
        db (Session): Active SQLAlchemy database session.
        user_id (str):Unique identifier of the customer.

    Raises:
        ValueError: If the customer is not found.

    Returns:
        list: List of purchased product details.
    """

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
    """Create a new customer.

    Args:
        db (Session): Active SQLAlchemy database session.
        customer (CustomerCreate): Customer data to be created.

    Returns:
        dict: Success message confirming customer creation.
    """

    create_customer_service(db, customer)

    return {"message": "Customer created successfully"}
