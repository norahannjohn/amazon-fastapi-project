from sqlalchemy.orm import Session

from app.schemas import SellerCreate

from app.mappers.seller_mapper import (
    get_sellers,
    get_seller_by_id,
    create_seller,
)


def get_sellers_service(db: Session):
    return get_sellers(db)


def get_seller_service(db: Session, seller_id: str):
    return get_seller_by_id(db, seller_id)


def create_seller_service(db: Session, seller: SellerCreate):
    return create_seller(db, seller)
