from sqlalchemy.orm import Session

from app.schemas import OrderCreate

from app.services.order_service import (
    get_orders_service,
    get_order_service,
    create_order_service,
)


def get_orders_handler(db: Session):
    """
    Retrieve all orders.

    Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of order objects.
    """
    return get_orders_service(db)


def get_order_handler(db: Session, order_id: int):
    """
    Retrieve an order by order ID.

    Args:
        db (Session): Active SQLAlchemy database session.
        order_id (int): Unique identifier of the order.

    Raises:
        ValueError: If the order is not found.

    Returns:
        Order: Order object.
    """

    order = get_order_service(db, order_id)

    if not order:
        raise ValueError("Order not found")

    return order


def create_order_handler(db: Session, order: OrderCreate):
    """
    Create a new order.

    Args:
        db (Session): Active SQLAlchemy database session.
        order (OrderCreate): Order data to be created.

    Returns:
        dict: Success message confirming order creation.
    """

    create_order_service(db, order)

    return {"message": "Order created successfully"}
