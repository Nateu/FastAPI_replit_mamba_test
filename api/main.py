from typing import Optional

from fastapi import FastAPI

app = FastAPI()

host = "https://fastapi.nateucodes.repl.co/"


@app.get("/")
def read_root():
    return {"skill_url": host + "skill/"}


@app.get("/skill/")
def read_skill():
    return {"skill": []}

@app.get("/skill/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
