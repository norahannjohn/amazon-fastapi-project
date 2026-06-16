from sqlalchemy.orm import Session

from app.schemas import SellerCreate

from app.services.seller_service import (
    get_sellers_service,
    get_seller_service,
    create_seller_service,
)


def get_sellers_handler(db: Session):
    """
    Retrieve all sellers.

    Args:
       db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of seller objects.
    """
    return get_sellers_service(db)


def get_seller_handler(db: Session, seller_id: str):
    """
    Retrieve a seller by seller ID.

    Args:
        db (Session): Active SQLAlchemy database session.
        seller_id (str): Unique identifier of the seller.

    Raises:
        ValueError: If the seller is not found.

    Returns:
        Seller: Seller object.
    """

    seller = get_seller_service(db, seller_id)

    if not seller:
        raise ValueError("Seller not found")

    return seller


def create_seller_handler(db: Session, seller: SellerCreate):
    """
    Create a new seller.

    Args:
        db (Session): Active SQLAlchemy database session.
        seller (SellerCreate): Seller data to be created.

    Returns:
        dict: Success message confirming seller creation.
    """

    create_seller_service(db, seller)

    return {"message": "Seller created successfully"}
