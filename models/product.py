from pydantic import BaseModel  # Importamos BaseModel para definir modelos con validación de datos

# Modelo de producto
class Product(BaseModel):
    id: int # Identificador único del producto, que debe ser un entero
    name: str # Nombre del producto, que debe ser un string
    price: float # Precio del producto, que debe ser un float