from sqlalchemy.orm import Session

from app.schemas import ProductCreate

from app.mappers.product_mapper import (
    get_products,
    get_product_by_id,
    create_product,
)


def get_products_service(db: Session):
    """
    Retrieve all products from the data access layer.

    Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
       list: List of product objects.
    """
    return get_products(db)


def get_product_service(db: Session, product_id: str):
    """
    Retrieve a product by product ID from the data access layer.

    Args:
        db (Session): Active SQLAlchemy database session.
        product_id (str): Unique identifier of the product.

    Returns:
        Product: Product object if found, otherwise None.
    """
    return get_product_by_id(db, product_id)


def create_product_service(db: Session, product: ProductCreate):
    """
    Create a new product in the database.

    Args:
        db (Session): Active SQLAlchemy database session.
        product (ProductCreate): Product data to be created.

    Returns:
        Product: Newly created product object.
    """
    return create_product(db, product)
