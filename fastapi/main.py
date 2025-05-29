
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, World!"}

print("FastAPI application is running...")

@app.get("/health")
def check():
    return {"status": "Healthy"}

@app.get("/items/{item_id}")
def items(item_id: int):
    return {"id": item_id}