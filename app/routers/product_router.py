from fastapi import APIRouter, HTTPException, status

from app.database import SessionLocal
from app.schemas import ProductCreate

from app.handlers.product_handler import (
    get_products_handler,
    get_product_handler,
    create_product_handler,
)

router = APIRouter()


@router.get("/products")
def get_products():

    db = SessionLocal()

    try:
        return get_products_handler(db)

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


@router.get("/products/{product_id}")
def get_product(product_id: str):

    db = SessionLocal()

    try:
        return get_product_handler(db, product_id)

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


@router.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):

    db = SessionLocal()

    try:
        return create_product_handler(db, product)

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
