from fastapi import APIRouter, HTTPException, status

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

    except RuntimeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@router.get("/sellers/{seller_id}")
def get_seller(seller_id: str):

    db = SessionLocal()

    try:
        return get_seller_handler(db, seller_id)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )

    except RuntimeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()


@router.post("/sellers", status_code=status.HTTP_201_CREATED)
def create_seller(seller: SellerCreate):

    db = SessionLocal()

    try:
        return create_seller_handler(db, seller)

    except RuntimeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error",
        )

    finally:
        db.close()
