
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Simple CRUD API")


# Define the structure of an item
class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)


class Item(ItemCreate):
    id: int


# Temporary in-memory storage
items: dict[int, Item] = {}
next_id = 1


# CREATE
@app.post("/items", response_model=Item, status_code=201)
def create_item(data: ItemCreate):
    global next_id

    item = Item(id=next_id, **data.model_dump())
    items[next_id] = item
    next_id += 1

    return item


# READ ALL
@app.get("/items", response_model=list[Item])
def get_items():
    return list(items.values())


# READ ONE
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = items.get(item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


# UPDATE
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, data: ItemCreate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_item = Item(id=item_id, **data.model_dump())
    items[item_id] = updated_item

    return updated_item


# DELETE
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    del items[item_id]
    return None
