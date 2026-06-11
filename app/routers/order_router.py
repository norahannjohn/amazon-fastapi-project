from fastapi import APIRouter

from app.database import SessionLocal
from app.schemas import OrderCreate

from app.handlers.order_handler import (
    get_orders_handler,
    get_order_handler,
    create_order_handler,
)

router = APIRouter()


@router.get("/orders")
def get_orders():

    db = SessionLocal()

    try:
        return get_orders_handler(db)

    finally:
        db.close()


@router.get("/orders/{order_id}")
def get_order(order_id: int):

    db = SessionLocal()

    try:
        return get_order_handler(db, order_id)

    finally:
        db.close()


@router.post("/orders", status_code=201)
def create_order(order: OrderCreate):

    db = SessionLocal()

    try:
        return create_order_handler(db, order)

    finally:
        db.close()
