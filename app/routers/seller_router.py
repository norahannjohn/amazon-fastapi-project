from fastapi import APIRouter

from app.database import SessionLocal
from app.schemas import SellerCreate

from app.handlers.seller_handler import (
    get_sellers_handler,
    get_seller_handler,
    create_seller_handler,
)

router = APIRouter()


@router.get("/sellers")
def get_sellers():

    db = SessionLocal()

    try:
        return get_sellers_handler(db)

    finally:
        db.close()


@router.get("/sellers/{seller_id}")
def get_seller(seller_id: str):

    db = SessionLocal()

    try:
        return get_seller_handler(db, seller_id)

    finally:
        db.close()


@router.post("/sellers", status_code=201)
def create_seller(seller: SellerCreate):

    db = SessionLocal()

    try:
        return create_seller_handler(db, seller)

    finally:
        db.close()
