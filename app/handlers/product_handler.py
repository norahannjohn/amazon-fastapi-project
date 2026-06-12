from sqlalchemy.orm import Session

from app.schemas import ProductCreate

from app.services.product_service import (
    get_products_service,
    get_product_service,
    create_product_service,
)


def get_products_handler(db: Session):
    return get_products_service(db)


def get_product_handler(db: Session, product_id: str):

    product = get_product_service(db, product_id)

    if not product:
        raise ValueError("Product not found")

    return product


def create_product_handler(db: Session, product: ProductCreate):

    create_product_service(db, product)

    return {"message": "Product created successfully"}
