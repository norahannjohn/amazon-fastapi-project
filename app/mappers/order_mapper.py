from sqlalchemy.orm import Session

from app.models import Order
from app.schemas import OrderCreate


def get_orders(db: Session):
    return db.query(Order).limit(10).all()


def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.order_id == order_id).first()


def create_order(db: Session, order: OrderCreate):

    new_order = Order(
        user_id=order.user_id,
        product_id=order.product_id,
        seller_id=order.seller_id,
        purchase_date=order.purchase_date,
        shipping_time_days=order.shipping_time_days,
        is_returned=order.is_returned,
        delivery_status=order.delivery_status,
    )

    db.add(new_order)
    db.commit()

    return new_order
