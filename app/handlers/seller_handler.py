from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas import SellerCreate

from app.services.seller_service import (
    get_sellers_service,
    get_seller_service,
    create_seller_service,
)


def get_sellers_handler(db: Session):

    try:
        return get_sellers_service(db)

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def get_seller_handler(db: Session, seller_id: str):

    try:

        seller = get_seller_service(db, seller_id)

        if not seller:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Seller not found",
            )

        return seller

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )


def create_seller_handler(db: Session, seller: SellerCreate):

    try:

        create_seller_service(db, seller)

        return {"message": "Seller created successfully"}

    except HTTPException:
        raise

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )
