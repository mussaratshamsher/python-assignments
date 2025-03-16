from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/itmes")
def create_item(item: str):
    item.append(item)
    return item
