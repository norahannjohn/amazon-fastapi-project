from sqlalchemy.orm import Session

from app.schemas import OrderCreate

from app.mappers.order_mapper import (
    get_orders,
    get_order_by_id,
    create_order,
)


def get_orders_service(db: Session):
    return get_orders(db)


def get_order_service(db: Session, order_id: int):
    return get_order_by_id(db, order_id)


def create_order_service(db: Session, order: OrderCreate):
    return create_order(db, order)
