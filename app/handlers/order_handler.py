from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas import OrderCreate

from app.services.order_service import (
    get_orders_service,
    get_order_service,
    create_order_service,
)


def get_orders_handler(db: Session):

    try:
        return get_orders_service(db)

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def get_order_handler(db: Session, order_id: int):

    try:

        order = get_order_service(db, order_id)

        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found",
            )

        return order

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def create_order_handler(db: Session, order: OrderCreate):

    try:

        create_order_service(db, order)

        return {"message": "Order created successfully"}

    except HTTPException:
        raise

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )
