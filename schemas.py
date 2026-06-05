from pydantic import BaseModel


class CustomerCreate(BaseModel):
    user_id: str
    location: str
    device: str
    payment_method: str