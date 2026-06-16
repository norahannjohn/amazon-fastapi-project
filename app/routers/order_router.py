from fastapi import APIRouter, HTTPException, status

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
    """
    Retrieve a list of orders.

    Returns:
        list: List of order records.

    Raises:
        HTTPException: If an internal server error occurs.
    """
    db = SessionLocal()

    try:
        return get_orders_handler(db)

    except RuntimeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@router.get("/orders/{order_id}")
def get_order(order_id: int):
    """
    Retrieve an order by order ID.

    Args:
        order_id (int): Unique identifier of the order.

    Returns:
        dict: Order details.

    Raises:
        HTTPException: If the order is not found.
        HTTPException: If an internal server error occurs.
    """
    db = SessionLocal()

    try:
        return get_order_handler(db, order_id)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )

    except RuntimeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@router.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate):
    """
    Create a new order.

    Args:
        order (OrderCreate): Order data to be created.

    Returns:
        dict: Success message confirming order creation.

    Raises:
        HTTPException: If an internal server error occurs.
    """
    db = SessionLocal()

    try:
        return create_order_handler(db, order)

    except RuntimeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()
