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
