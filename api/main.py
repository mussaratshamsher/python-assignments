
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

# Defining the item model
class item(BaseModel):
    id: int
    name: str
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
    3: Product(name="Tablet", id=3, price=299.99, features=["4GB RAM", "64GB Storage", "10-inch Display"], availability=True, details="Portable tablet for reading and browsing."),
    4: Product(name="Smartwatch", id=4, price=199.99, features=["Heart Rate Monitor", "GPS", "Water Resistant"], availability=True, details="Stylish smartwatch with fitness tracking capabilities."),
    5: Product(name="Headphones", id=5, price=89.99, features=["Noise Cancelling", "Wireless", "20-hour Battery"], availability=True, details="Comfortable headphones with excellent sound quality.")
}
items = {
   1: item(id=1, name="Lipstick", price=200, features=["Long-lasting", "Matte finish"], availability=True, details="A vibrant red lipstick perfect for any occasion."),
   2: item(id=2, name="Foundation", price=300, features=["Full coverage", "Hydrating"], availability=True, details="A lightweight foundation that provides full coverage and hydration."),
   3: item(id=3, name="Eyeliner", price=150, features=["Waterproof", "Precision tip"], availability=True, details="A waterproof eyeliner with a precision tip for easy application."),
   4: item(id=4, name="Mascara", price=250, features=["Volumizing", "Lengthening"], availability=True, details="A volumizing mascara that lengthens and defines lashes."),
   5: item(id=5, name="Blush", price=180, features=["Natural finish", "Buildable coverage"], availability=True, details="A blush that provides a natural finish and buildable coverage.")
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


# Endpoint to get all Items
@app.get("/items", response_model=List[item])
def get_items():
    return list(items.values())

# Endpoint to get a specific item by ID
@app.get("/items/{id}", response_model=item)
async def get_item(id: int):
    if id not in items:
        return {"error": "item not found"}
    return items[id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

