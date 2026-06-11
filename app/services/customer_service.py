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
    return get_customers(db)


def get_customer_service(db: Session, user_id: str):
    return get_customer_by_id(db, user_id)


def get_customer_orders_service(db: Session, user_id: str):
    return get_customer_orders(db, user_id)


def get_customer_purchases_service(db: Session, user_id: str):
    return get_customer_purchases(db, user_id)


def create_customer_service(db: Session, customer: CustomerCreate):
    return create_customer(db, customer)
