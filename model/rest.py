#Classe para crear el modelo o los campos que va a llevar
from pydantic import BaseModel,Field
from enum import Enum

class Item(BaseModel):
    nombre:str
    apellido:str
    cantidad:int
    
class ModelName(str,Enum):
    alexnet= "alexnet"
    resnet = "resnet"
    lenete = "lenet"

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
