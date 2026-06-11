from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas import ProductCreate

from app.services.product_service import (
    get_products_service,
    get_product_service,
    create_product_service,
)


def get_products_handler(db: Session):

    try:
        return get_products_service(db)

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def get_product_handler(db: Session, product_id: str):

    try:

        product = get_product_service(db, product_id)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        return product

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def create_product_handler(db: Session, product: ProductCreate):

    try:

        create_product_service(db, product)

        return {"message": "Product created successfully"}

    except HTTPException:
        raise

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )
