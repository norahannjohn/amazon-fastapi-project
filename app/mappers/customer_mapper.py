from sqlalchemy.orm import Session

from app.models import Customer
from app.schemas import CustomerCreate


def get_customers(db: Session):
    return db.query(Customer).limit(10).all()


def get_customer_by_id(db: Session, user_id: str):
    return db.query(Customer).filter(Customer.user_id == user_id).first()


def get_customer_orders(db: Session, user_id: str):

    customer = db.query(Customer).filter(Customer.user_id == user_id).first()

    return customer


def get_customer_purchases(db: Session, user_id: str):

    customer = db.query(Customer).filter(Customer.user_id == user_id).first()

    return customer


def create_customer(db: Session, customer: CustomerCreate):

    new_customer = Customer(
        user_id=customer.user_id,
        location=customer.location,
        device=customer.device,
        payment_method=customer.payment_method,
    )

    db.add(new_customer)

    db.commit()

    return new_customer
