from sqlalchemy.orm import Session

from app.models import Customer
from app.schemas import CustomerCreate


def get_customers(db: Session):
    """
    Retrieve a list of customers from the database.

    Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of customer records.

    Raises:
        RuntimeError: If a database error occurs while fetching customers.
    """
    try:
        return db.query(Customer).limit(10).all()

    except Exception:
        raise RuntimeError("Database error while fetching customers")


def get_customer_by_id(db: Session, user_id: str):
    """
    Retrieve a customer from the database by user ID.

    Args:
        db (Session): Active SQLAlchemy database session.
        user_id (str): Unique identifier of the customer.

    Returns:
        Customer | None: Matching customer record if found.

    Raises:
        RuntimeError: If a database error occurs while fetching the customer.
    """
    try:
        return db.query(Customer).filter(Customer.user_id == user_id).first()

    except Exception:
        raise RuntimeError("Database error while fetching customer")


def get_customer_orders(db: Session, user_id: str):
    """
    Retrieve a customer and associated orders from the database.

    Args:
        db (Session): Active SQLAlchemy database session.
        user_id (str): Unique identifier of the customer.

    Returns:
        Customer | None: Customer record with related orders if found.

    Raises:
        RuntimeError: If a database error occurs while fetching customer orders.
    """
    try:
        customer = db.query(Customer).filter(Customer.user_id == user_id).first()
        return customer

    except Exception:
        raise RuntimeError("Database error while fetching customer orders")


def get_customer_purchases(db: Session, user_id: str):
    """
    Retrieve a customer and associated purchases from the database.

    Args:
        db (Session): Active SQLAlchemy database session.
        user_id (str): Unique identifier of the customer.

    Returns:
        Customer | None: Customer record with related purchase information if found.

    Raises:
        RuntimeError: If a database error occurs while fetching customer purchases.
    """
    try:
        customer = db.query(Customer).filter(Customer.user_id == user_id).first()
        return customer

    except Exception:
        raise RuntimeError("Database error while fetching customer purchases")


def create_customer(db: Session, customer: CustomerCreate):
    """
    Create a new customer in the database.

    Args:
        db (Session): Active SQLAlchemy database session.
        customer (CustomerCreate): Customer data to be stored.

    Returns:
        Customer: Newly created customer record.

    Raises:
        RuntimeError: If a database error occurs while creating the customer.
    """
    try:

        new_customer = Customer(
            user_id=customer.user_id,
            location=customer.location,
            device=customer.device,
            payment_method=customer.payment_method,
        )

        db.add(new_customer)
        db.commit()

        return new_customer

    except Exception:

        db.rollback()

        raise RuntimeError("Database error while creating customer")
