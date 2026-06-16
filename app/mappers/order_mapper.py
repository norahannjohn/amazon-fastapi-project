from sqlalchemy.orm import Session

from app.models import Order
from app.schemas import OrderCreate


def get_orders(db: Session):
    """
    Retrieve a list of orders from the database.

    Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of order records.

    Raises:
        RuntimeError: If a database error occurs while fetching orders.
    """
    try:
        return db.query(Order).limit(10).all()

    except Exception:
        raise RuntimeError("Database error while fetching orders")


def get_order_by_id(db: Session, order_id: int):
    """
    Retrieve an order from the database by order ID.

    Args:
        db (Session): Active SQLAlchemy database session.
        order_id (int): Unique identifier of the order.

    Returns:
        Order | None: Matching order record if found.

    Raises:
        RuntimeError: If a database error occurs while fetching the order.
    """
    try:
        return db.query(Order).filter(Order.order_id == order_id).first()

    except Exception:
        raise RuntimeError("Database error while fetching order")


def create_order(db: Session, order: OrderCreate):
    """
    Create a new order in the database.

    Args:
        db (Session): Active SQLAlchemy database session.
        order (OrderCreate): Order data to be stored.

    Returns:
        Order: Newly created order record.

    Raises:
        RuntimeError: If a database error occurs while creating the order.
    """
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

        return new_order

    except Exception:

        db.rollback()

        raise RuntimeError("Database error while creating order")
