from sqlalchemy.orm import Session

from app.schemas import OrderCreate

from app.mappers.order_mapper import (
    get_orders,
    get_order_by_id,
    create_order,
)


def get_orders_service(db: Session):
    """
    Retrieve all orders from the data access layer.

    Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of order objects.
    """
    return get_orders(db)


def get_order_service(db: Session, order_id: int):
    """
    Retrieve an order by order ID from the data access layer.

    Args:
        db (Session): Active SQLAlchemy database session.
        order_id (int): Unique identifier of the order.

    Returns:
        Order: Order object if found, otherwise None.
    """
    return get_order_by_id(db, order_id)


def create_order_service(db: Session, order: OrderCreate):
    """
    Create a new order in the database.

    Args:
        db (Session): Active SQLAlchemy database session.
        order (OrderCreate): Order data to be created.

    Returns:
        Order: Newly created order object.
    """
    return create_order(db, order)
