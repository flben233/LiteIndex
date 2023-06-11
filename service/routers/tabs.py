import json
import os

from fastapi import APIRouter
from pydantic import BaseModel

from config import IMAGE_PATH

app = APIRouter()

items = []


class Item(BaseModel):
    name: str
    url: str
    icon: str


@app.post("/api/items/put/")
async def create_item(item: Item):
    items.append(item.dict())
    with open("items.json", "w") as j:
        json.dump(items, j)
    return {"status": "success"}


@app.get("/api/items/read/")
async def read_items():
    return items


@app.post("/api/items/delete/")
async def del_item(item: Item):
    items.remove(item.dict())
    icon_name = item.icon.split("/")[-1]
    os.remove(f"{IMAGE_PATH}/{icon_name}")
    with open("items.json", "w") as j:
        json.dump(items, j)
    return {"status": "success"}
