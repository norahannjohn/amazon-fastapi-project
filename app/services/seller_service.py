from sqlalchemy.orm import Session

from app.schemas import SellerCreate

from app.mappers.seller_mapper import (
    get_sellers,
    get_seller_by_id,
    create_seller,
)


def get_sellers_service(db: Session):
    """
        Retrieve all sellers from the data access layer.

        Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of seller objects.
    """
    return get_sellers(db)


def get_seller_service(db: Session, seller_id: str):
    """
    Retrieve a seller by seller ID from the data access layer.

    Args:
        db (Session): Active SQLAlchemy database session.
        seller_id (str): Unique identifier of the seller.

    Returns:
        Seller: Seller object if found, otherwise None.
    """
    return get_seller_by_id(db, seller_id)


def create_seller_service(db: Session, seller: SellerCreate):
    """
    Create a new seller in the database.

    Args:
        db (Session): Active SQLAlchemy database session.
        seller (SellerCreate): Seller data to be created.

    Returns:
        Seller: Newly created seller object.
    """
    return create_seller(db, seller)
