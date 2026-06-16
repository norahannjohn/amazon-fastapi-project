from sqlalchemy.orm import Session

from app.models import Product
from app.schemas import ProductCreate


def get_products(db: Session):
    """
    Retrieve a list of products from the database.

    Args:
        db (Session): Active SQLAlchemy database session.

    Returns:
        list: List of product records.

    Raises:
        RuntimeError: If a database error occurs while fetching products.
    """
    try:
        return db.query(Product).limit(10).all()

    except Exception:
        raise RuntimeError("Database error while fetching products")


def get_product_by_id(db: Session, product_id: str):
    """
    Retrieve a product from the database by product ID.

    Args:
        db (Session): Active SQLAlchemy database session.
        product_id (str): Unique identifier of the product.

    Returns:
        Product | None: Matching product record if found.

    Raises:
        RuntimeError: If a database error occurs while fetching the product.
    """
    try:
        return db.query(Product).filter(Product.product_id == product_id).first()

    except Exception:
        raise RuntimeError("Database error while fetching product")


def create_product(db: Session, product: ProductCreate):
    """
    Create a new product in the database.

    Args:
        db (Session): Active SQLAlchemy database session.
        product (ProductCreate): Product data to be stored.

    Returns:
        Product: Newly created product record.

    Raises:
        RuntimeError: If a database error occurs while creating the product.
    """
    try:

        new_product = Product(
            product_id=product.product_id,
            category=product.category,
            subcategory=product.subcategory,
            brand=product.brand,
            price=product.price,
            discount=product.discount,
            final_price=product.final_price,
            rating=product.rating,
            review_count=product.review_count,
            stock=product.stock,
        )

        db.add(new_product)
        db.commit()

        return new_product

    except Exception:

        db.rollback()

        raise RuntimeError("Database error while creating product")
