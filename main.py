from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_items_db = [{"item_name": "Foo"},
                 {"item_name": "Bar"},
                 {"item_name": "Baz"}]


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/items/")
async def read_items(sort: Optional[str], skip: int = 0, limit: int = 10):
    print(skip + limit)
    return fake_items_db[skip: skip + limit]


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return blog
