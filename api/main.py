
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Define the Product model
class Product(BaseModel):
    name: str
    id: int
    price: float
    features: List[str]
    availability: bool
    details: str

# Initialize the FastAPI app
app = FastAPI()

# Sample data (in a real application, this could be fetched from a database)
products = {
    1: Product(name="Laptop", id=1, price=999.99, features=["16GB RAM", "512GB SSD", "Intel i7"], availability=True, details="High-performance laptop for gaming and work."),
    2: Product(name="Smartphone", id=2, price=499.99, features=["6GB RAM", "128GB Storage", "OLED Display"], availability=False, details="Affordable smartphone with great features."),
}

# Endpoint to get all products
@app.get("/products", response_model=List[Product])
async def get_products():
    return list(products.values())

# Endpoint to get a specific product by ID
@app.get("/products/{id}", response_model=Product)
async def get_product(id: int):
    if id not in products:
        return {"error": "Product not found"}
    return products[id]

# Endpoint to add a new product (for example, for testing purposes)
@app.post("/products", response_model=Product)
async def create_product(product: Product):
    id = len(products) + 1  # Simple ID generation
    products[id] = product
    return product

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

