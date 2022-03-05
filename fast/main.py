from enum import Enum
from typing import Optional
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field

app = FastAPI()  # 建立一個 Fast API application


@app.get("/")  # 指定 api 路徑 (get方法)
def read_root():
    return {"Hello": "Worldaaa"}


@app.get("/users/{user_id}")  # 指定 api 路徑 (get方法)
def read_user(user_id: int, q: Optional[str] = None):
    return {"user_id": user_id, "q": q}


@app.get("/query_param_str")
async def query_param_str(pID: str):  # 轉換成字串
    return {"user": pID}


@app.get("/query_param_int")
async def query_param_int(pID: int):  # 轉換成整數
    return {"user": pID}


@app.get("/default_param")
async def query_param_str(param_a: str, param_b: str = "example"):  # 轉換成字串
    return {"param_a": param_a, "param_b": param_b}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


# @app.post("/items/")
# async def create_item(item: Item):
#     return item
# async def create_item(item: Item):
#     if item.price > 100:
#         return "太贵了"
#     return item

# @app.get("/items/")
# def read(paword: str = Query(..., min_length=8, max_length=16)):
#     results = {"items": [{"oneid": "shanghai"}, {"two": "beijing"}]}
#     if paword:
#         results.update({"paword": paword})
#     return results
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items")
def update_item(item: Optional[Item]):
    result = {}
    if item.tax is not None:
        total = item.price*item.tax
        result['price'] = total
        result['name'] = item.name
        return result
    result['price'] = item.price
    result['name'] = item.name
    return result
