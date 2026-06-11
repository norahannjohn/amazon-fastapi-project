from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas import CustomerCreate

from app.services.customer_service import (
    get_customers_service,
    get_customer_service,
    get_customer_orders_service,
    get_customer_purchases_service,
    create_customer_service,
)


def get_customers_handler(db: Session):
    """
    Retrieve the list of customers.

    Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of customer objects.

    Raises:
        HTTPException: If an internal server error occurs.
    """

    try:
        return get_customers_service(db)

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def get_customer_handler(db: Session, user_id: str):

    try:

        customer = get_customer_service(db, user_id)

        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found",
            )

        return customer

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def get_customer_orders_handler(db: Session, user_id: str):

    try:

        customer = get_customer_orders_service(db, user_id)

        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found",
            )

        result = []

        for order in customer.orders:
            result.append(
                {
                    "order_id": order.order_id,
                    "user_id": order.user_id,
                    "product_id": order.product_id,
                    "seller_id": order.seller_id,
                    "purchase_date": str(order.purchase_date),
                    "shipping_time_days": order.shipping_time_days,
                    "is_returned": order.is_returned,
                    "delivery_status": order.delivery_status,
                }
            )

        return result

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def get_customer_purchases_handler(db: Session, user_id: str):

    try:

        customer = get_customer_purchases_service(db, user_id)

        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found",
            )

        result = []

        for order in customer.orders:
            result.append(
                {
                    "order_id": order.order_id,
                    "purchase_date": str(order.purchase_date),
                    "delivery_status": order.delivery_status,
                    "product_id": order.product.product_id,
                    "brand": order.product.brand,
                    "category": order.product.category,
                    "final_price": order.product.final_price,
                    "rating": order.product.rating,
                }
            )

        return result

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def create_customer_handler(db: Session, customer: CustomerCreate):

    try:

        create_customer_service(db, customer)

        return {"message": "Customer created successfully"}

    except HTTPException:
        raise

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )
