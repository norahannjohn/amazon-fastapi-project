from sqlalchemy.orm import Session

from app.schemas import ProductCreate

from app.services.product_service import (
    get_products_service,
    get_product_service,
    create_product_service,
)


def get_products_handler(db: Session):
    """
    Retrieve all products.

    Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of product objects.
    """
    return get_products_service(db)


def get_product_handler(db: Session, product_id: str):
    """
    Retrieve a product by product ID.

    Args:
        db (Session): Active SQLAlchemy database session.
        product_id (str): Unique identifier of the product.

    Raises:
        ValueError: If the product is not found.

    Returns:
        Product: Product object.
    """

    product = get_product_service(db, product_id)

    if not product:
        raise ValueError("Product not found")

    return product


def create_product_handler(db: Session, product: ProductCreate):
    """
    Create a new product.

    Args:
        db (Session): Active SQLAlchemy database session.
        product (ProductCreate): Product data to be created.

    Returns:
        dict: Success message confirming product creation.
    """

    create_product_service(db, product)

    return {"message": "Product created successfully"}
