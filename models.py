from database import Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey


class Customer(Base):
    __tablename__ = "customers"

    user_id = Column(String, primary_key=True)
    location = Column(String)
    device = Column(String)
    payment_method = Column(String)

class Product(Base):
    __tablename__ = "products"

    product_id = Column(String, primary_key=True)
    category = Column(String)
    subcategory = Column(String)
    brand = Column(String)

    price = Column(Float)
    discount = Column(Float)
    final_price = Column(Float)

    rating = Column(Float)
    review_count = Column(Integer)

    stock = Column(Integer)

class Seller(Base):
    __tablename__ = "sellers"

    seller_id = Column(String, primary_key=True)
    seller_rating = Column(Float)

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(String, ForeignKey("customers.user_id"))
    product_id = Column(String, ForeignKey("products.product_id"))
    seller_id = Column(String, ForeignKey("sellers.seller_id"))

    purchase_date = Column(String)
    shipping_time_days = Column(Integer)

    is_returned = Column(String)
    delivery_status = Column(String)