from database import engine, Base
from models import Customer, Product, Seller, Order

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")