from pydantic import BaseModel # Importamos BaseModel para definir modelos de datos con validación
from typing import List # Importamos List para poder tipar las listas

# Modelo de pedido (solo para insertar)
class Order(BaseModel):
    id: int # Identificador del pedido, debe ser un entero
    products: List[int] # Lista de ids de producto incluidos en el pedido
