"""
lance une API minimale
"""
from fastapi import FastAPI

app = FastAPI(
    title="une API minimale"
    ,root_path="/proxy/8000/")

@app.get("/")
def read_root():
    """endpoint racine

    Returns:
        _type_: _description_
    """
    return {"Hello": "Mathieu"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """API minimale

    Args:
        item_id (int): _description_
        q (str, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    return {"item_id": item_id, "q": q}
