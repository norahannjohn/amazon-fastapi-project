from fastapi import APIRouter, HTTPException, status

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
    """_summary_

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        _type_: _description_
    """

    db = SessionLocal()

    try:
        return get_customers_handler(db)

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


@router.get("/customers/{user_id}")
def get_customer(user_id: str):
    """_summary_

    Args:
        user_id (str): _description_

    Raises:
        HTTPException: _description_
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        _type_: _description_
    """

    db = SessionLocal()

    try:
        return get_customer_handler(db, user_id)

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


@router.get("/customers/{user_id}/orders")
def get_customer_orders(user_id: str):

    db = SessionLocal()

    try:
        return get_customer_orders_handler(db, user_id)

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


@router.get("/customers/{user_id}/purchases")
def get_customer_purchases(user_id: str):

    db = SessionLocal()

    try:
        return get_customer_purchases_handler(db, user_id)

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


@router.post("/customers", status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreate):

    db = SessionLocal()

    try:
        return create_customer_handler(db, customer)

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
