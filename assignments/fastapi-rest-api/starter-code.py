# Starter Code: FastAPI REST API

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

items: List[Item] = []

@app.post('/items/', response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.get('/items/', response_model=List[Item])
def list_items(q: Optional[str] = None, limit: Optional[int] = 10):
    results = items
    if q:
        results = [item for item in results if q.lower() in item.name.lower() or (item.description and q.lower() in item.description.lower())]
    return results[:limit]

@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail='Item not found')

@app.put('/items/{item_id}', response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail='Item not found')

@app.delete('/items/{item_id}')
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {'detail': 'Item deleted'}
    raise HTTPException(status_code=404, detail='Item not found')
