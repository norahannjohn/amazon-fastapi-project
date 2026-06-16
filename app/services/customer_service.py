from sqlalchemy.orm import Session

from app.schemas import CustomerCreate

from app.mappers.customer_mapper import (
    get_customers,
    get_customer_by_id,
    get_customer_orders,
    get_customer_purchases,
    create_customer,
)


def get_customers_service(db: Session):
    """
    Retrieve all customers from the data access layer.

    Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of customer objects.
    """
    return get_customers(db)


def get_customer_service(db: Session, user_id: str):
    """
    Retrieve a customer by user ID from the data access layer.

    Args:
        db (Session): Active SQLAlchemy database session.
        user_id (str): Unique identifier of the customer.

    Returns:
        Customer: Customer object if found, otherwise None.
    """
    return get_customer_by_id(db, user_id)


def get_customer_orders_service(db: Session, user_id: str):
    """
    Retrieve all orders for a customer from the data access layer.

    Args:
        db (Session): Active SQLAlchemy database session.
        user_id (str): Unique identifier of the customer.

    Returns:
        Customer: Customer object containing associated orders.
    """
    return get_customer_orders(db, user_id)


def get_customer_purchases_service(db: Session, user_id: str):
    """
    Retrieve the purchase history of a customer from the data access layer.

    Args:
        db (Session): Active SQLAlchemy database session.
        user_id (str): Unique identifier of the customer.

    Returns:
        Customer: Customer object containing purchase details.
    """
    return get_customer_purchases(db, user_id)


def create_customer_service(db: Session, customer: CustomerCreate):
    """
    Create a new customer in the database.

    Args:
        db (Session): Active SQLAlchemy database session.
        customer (CustomerCreate): Customer data to be created.

    Returns:
        Customer: Newly created customer object.
    """
    return create_customer(db, customer)
