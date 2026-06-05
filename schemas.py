from pydantic import BaseModel


class CustomerCreate(BaseModel):
    user_id: str
    location: str
    device: str
    payment_method: str

class OrderCreate(BaseModel):
    user_id: str
    product_id: str
    seller_id: str

    purchase_date: str
    shipping_time_days: int

    is_returned: str
    delivery_status: str

class ProductCreate(BaseModel):
    product_id: str
    category: str
    subcategory: str
    brand: str

    price: float
    discount: float
    final_price: float

    rating: float
    review_count: int

    stock: int