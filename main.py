#Clases para crear la api y las rutas
from fastapi import FastAPI
from model.rest import Item,ModelName,fake_items_db

app=FastAPI()

#Creando un campo Enum con get
@app.get("/models/{model_name}")
async def obtener_modelos(model_name:ModelName):
    if model_name == ModelName.alexnet:
        return{"Model_name":model_name, "Message":"HOla alexnet" }
    
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]