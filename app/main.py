from fastapi import FastAPI

from app.routers.customer_router import router as customer_router
from app.routers.product_router import router as product_router
from app.routers.seller_router import router as seller_router
from app.routers.order_router import router as order_router

app = FastAPI()

app.include_router(customer_router)
app.include_router(product_router)
app.include_router(seller_router)
app.include_router(order_router)


@app.get("/")
def home():
    """
    Home endpoint to verify that the API is running.

    Returns:
        dict: Success message indicating the API is running.
    """
    return {"message": "Amazon E-commerce API is running"}
