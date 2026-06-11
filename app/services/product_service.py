from sqlalchemy.orm import Session

from app.schemas import ProductCreate

from app.mappers.product_mapper import (
    get_products,
    get_product_by_id,
    create_product,
)


def get_products_service(db: Session):
    return get_products(db)


def get_product_service(db: Session, product_id: str):
    return get_product_by_id(db, product_id)


def create_product_service(db: Session, product: ProductCreate):
    return create_product(db, product)
