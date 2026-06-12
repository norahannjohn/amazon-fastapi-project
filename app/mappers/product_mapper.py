from sqlalchemy.orm import Session

from app.models import Product
from app.schemas import ProductCreate


def get_products(db: Session):

    try:
        return db.query(Product).limit(10).all()

    except Exception:
        raise RuntimeError("Database error while fetching products")


def get_product_by_id(db: Session, product_id: str):

    try:
        return db.query(Product).filter(Product.product_id == product_id).first()

    except Exception:
        raise RuntimeError("Database error while fetching product")


def create_product(db: Session, product: ProductCreate):

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
