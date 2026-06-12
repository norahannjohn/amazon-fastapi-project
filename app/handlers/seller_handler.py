from sqlalchemy.orm import Session

from app.schemas import SellerCreate

from app.services.seller_service import (
    get_sellers_service,
    get_seller_service,
    create_seller_service,
)


def get_sellers_handler(db: Session):
    return get_sellers_service(db)


def get_seller_handler(db: Session, seller_id: str):

    seller = get_seller_service(db, seller_id)

    if not seller:
        raise ValueError("Seller not found")

    return seller


def create_seller_handler(db: Session, seller: SellerCreate):

    create_seller_service(db, seller)

    return {"message": "Seller created successfully"}
