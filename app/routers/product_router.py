from fastapi import APIRouter

from app.database import SessionLocal
from app.schemas import ProductCreate

from app.handlers.product_handler import (
    get_products_handler,
    get_product_handler,
    create_product_handler,
)

router = APIRouter()


@router.get("/products")
def get_products():

    db = SessionLocal()

    try:
        return get_products_handler(db)

    finally:
        db.close()


@router.get("/products/{product_id}")
def get_product(product_id: str):

    db = SessionLocal()

    try:
        return get_product_handler(db, product_id)

    finally:
        db.close()


@router.post("/products", status_code=201)
def create_product(product: ProductCreate):

    db = SessionLocal()

    try:
        return create_product_handler(db, product)

    finally:
        db.close()
