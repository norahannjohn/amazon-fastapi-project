from sqlalchemy.orm import Session

from app.models import Customer
from app.schemas import CustomerCreate


def get_customers(db: Session):

    try:
        return db.query(Customer).limit(10).all()

    except Exception:
        raise RuntimeError("Database error while fetching customers")


def get_customer_by_id(db: Session, user_id: str):

    try:
        return db.query(Customer).filter(Customer.user_id == user_id).first()

    except Exception:
        raise RuntimeError("Database error while fetching customer")


def get_customer_orders(db: Session, user_id: str):

    try:
        customer = db.query(Customer).filter(Customer.user_id == user_id).first()
        return customer

    except Exception:
        raise RuntimeError("Database error while fetching customer orders")


def get_customer_purchases(db: Session, user_id: str):

    try:
        customer = db.query(Customer).filter(Customer.user_id == user_id).first()
        return customer

    except Exception:
        raise RuntimeError("Database error while fetching customer purchases")


def create_customer(db: Session, customer: CustomerCreate):

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
