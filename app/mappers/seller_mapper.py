from sqlalchemy.orm import Session

from app.models import Seller
from app.schemas import SellerCreate


def get_sellers(db: Session):

    try:
        return db.query(Seller).limit(10).all()

    except Exception:
        raise RuntimeError("Database error while fetching sellers")


def get_seller_by_id(db: Session, seller_id: str):

    try:
        return db.query(Seller).filter(Seller.seller_id == seller_id).first()

    except Exception:
        raise RuntimeError("Database error while fetching seller")


def create_seller(db: Session, seller: SellerCreate):

    try:

        new_seller = Seller(
            seller_id=seller.seller_id,
            seller_rating=seller.seller_rating,
        )

        db.add(new_seller)
        db.commit()

        return new_seller

    except Exception:

        db.rollback()

        raise RuntimeError("Database error while creating seller")
