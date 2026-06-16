from sqlalchemy.orm import Session

from app.models import Seller
from app.schemas import SellerCreate


def get_sellers(db: Session):
    """
    Retrieve a list of sellers from the database.

    Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of seller records.

    Raises:
        RuntimeError: If a database error occurs while fetching sellers.
    """
    try:
        return db.query(Seller).limit(10).all()

    except Exception:
        raise RuntimeError("Database error while fetching sellers")


def get_seller_by_id(db: Session, seller_id: str):
    """
    Retrieve a seller from the database by seller ID.

    Args:
        db (Session): Active SQLAlchemy database session.
        seller_id (str): Unique identifier of the seller.

    Returns:
        Seller | None: Matching seller record if found.

    Raises:
        RuntimeError: If a database error occurs while fetching the seller.
    """
    try:
        return db.query(Seller).filter(Seller.seller_id == seller_id).first()

    except Exception:
        raise RuntimeError("Database error while fetching seller")


def create_seller(db: Session, seller: SellerCreate):
    """
    Create a new seller in the database.

    Args:
        db (Session): Active SQLAlchemy database session.
        seller (SellerCreate): Seller data to be stored.

    Returns:
        Seller: Newly created seller record.

    Raises:
        RuntimeError: If a database error occurs while creating the seller.
    """
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
