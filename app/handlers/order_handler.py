from sqlalchemy.orm import Session

from app.schemas import OrderCreate

from app.services.order_service import (
    get_orders_service,
    get_order_service,
    create_order_service,
)


def get_orders_handler(db: Session):
    return get_orders_service(db)


def get_order_handler(db: Session, order_id: int):

    order = get_order_service(db, order_id)

    if not order:
        raise ValueError("Order not found")

    return order


def create_order_handler(db: Session, order: OrderCreate):

    create_order_service(db, order)

    return {"message": "Order created successfully"}
