from fastapi import APIRouter

from app.database import SessionLocal
from app.schemas import CustomerCreate
from app.handlers.customer_handler import (
    get_customers_handler,
    get_customer_handler,
    get_customer_orders_handler,
    get_customer_purchases_handler,
    create_customer_handler,
)

router = APIRouter()


@router.get("/customers")
def get_customers():

    db = SessionLocal()

    try:
        return get_customers_handler(db)

    finally:
        db.close()


@router.get("/customers/{user_id}")
def get_customer(user_id: str):

    db = SessionLocal()

    try:
        return get_customer_handler(db, user_id)

    finally:
        db.close()


@router.get("/customers/{user_id}/orders")
def get_customer_orders(user_id: str):

    db = SessionLocal()

    try:
        return get_customer_orders_handler(db, user_id)

    finally:
        db.close()


@router.get("/customers/{user_id}/purchases")
def get_customer_purchases(user_id: str):

    db = SessionLocal()

    try:
        return get_customer_purchases_handler(db, user_id)

    finally:
        db.close()


@router.post("/customers", status_code=201)
def create_customer(customer: CustomerCreate):

    db = SessionLocal()

    try:
        return create_customer_handler(db, customer)

    finally:
        db.close()
