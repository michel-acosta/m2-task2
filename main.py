from fastapi import FastAPI  # Importamos FastAPI para crear la aplicación
from fastapi import status # Importamos status para códigos de estado HTTP
from fastapi.exceptions import HTTPException # Importamos HTTPException para manejar errores HTTP

from models.product import Product  # Modelo de producto
from models.order import Order  # Modelo de pedido
from data.bst_products import product_tree  # Árbol binario de productos
from data.linkedlist_orders import order_list  # Lista enlazada de pedidos

app = FastAPI() 

# ENDPOINTS PARA PRODUCTOS

# Crea un producto y lo inserta en un árbol binario
@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    
    # Comprobamos si ya existe un producto con el mismo id
    if product_tree.search(product.id):
        raise HTTPException(status_code=400, detail="Product id already exists")
    
    # Insertar el producto en el árbol binario
    product_tree.insert(product)
    
    # Devolvemos resultado éxitoso
    return {"message":"Product created", "product": product}

# Buscamos un producto por su id
@app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
def get_product(product_id: int):
    
    # Buscamos el producto en el árbol binario
    product = product_tree.search(product_id)
    
    # Si no existe, lanzar error 404
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Devolver el producto encontrado
    return {"product": product}

@app.get("/products", status_code=status.HTTP_200_OK)
def list_products():
    # Devolver la lista de productos completa
    return {"products": getProductsInOrder(product_tree.root)}

@app.put("/products/{product_id}", status_code=status.HTTP_200_OK)
def update_product(product_id: int, updated: Product):

    # Verificar que el id coincide
    if product_id != updated.id:
        raise HTTPException(status_code=400, detail="Product id mismatch")

    # Verificar que el producto existe
    product_exists = product_tree.search(product_id)
    if not product_exists:
        raise HTTPException(status_code=404, detail="Product not found")

    # Reemplazar el producto
    product_tree.update(updated)

    return {"message": "Product updated", "product": updated}

@app.delete("/products/{product_id}", status_code=status.HTTP_200_OK)
def delete_product(product_id: int):

    # Verificar que el producto existe
    product_exists = product_tree.search(product_id)
    if not product_exists:
        raise HTTPException(status_code=404, detail="Product not found")

    # Eliminar el producto
    deleted = product_tree.delete(product_id)

    if not deleted:
        raise HTTPException(status_code=500, detail="Error deleting product")

    return {"message": "Product deleted"}

# MÉTODOS AUXILIARES PARA PRODUCTOS

def getProductsInOrder(node):
    # Recorre el árbol en orden y devuelve una lista de productos
    if not node:
        return []
    
    leftInOrder = getProductsInOrder(node.left) # Recorremos el subárbol izquierdo
    rightInOrder = getProductsInOrder(node.right) # Recorremos el subárbol derecho
    mySelf = [node.product.model_dump()] # Convertimos el producto a diccionario

    return leftInOrder + mySelf + rightInOrder # Concatenamos las listas

# ENDPOINTS PARA PEDIDOS

@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(order: Order):
    # Crear un nuevo pedido y añadirlo a la lista enlazada
    
    order_products = []

    # Validar que todos los IDs de productos existan en el árbol
    for pid in order.products:
        product = product_tree.search(pid)
        if not product:
            raise HTTPException(
                status_code=400,
                detail=f"Product with ID {pid} does not exist"
            )
        order_products.append(product.model_dump())
    
    # Creamos un objeto "Order" interno con productos completos
    full_order = {
        "id": order.id,
        "products": order_products
    }

    # Añadir el pedido a la lista enlazada
    order_list.add(full_order)
    
    # Devolver mensaje de éxito
    return {"message": "Order created", "order": full_order}

@app.get("/orders/{order_id}", status_code=status.HTTP_200_OK)
def get_order(order_id: int):
    # Buscar un pedido por su id
    
    # Buscar el pedido en la lista enlazada
    order = order_list.get_by_id(order_id)
    
    # Si no existe, lanzar error 404
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Devolver el pedido encontrado
    return {"order": order}

@app.put("/orders/{order_id}", status_code=status.HTTP_200_OK)
def update_order(order_id: int, updated: Order):
    # Actualizar un pedido existente por su id
    
    # Validar que el ID del pedido coincida con el ID del objeto enviado
    if order_id != updated.id:
        raise HTTPException(status_code=400, detail="Order ID mismatch")

    order_products = []

    for pid in updated.products:
        product = product_tree.search(pid)
        if not product:
            raise HTTPException(
                status_code=400,
                detail=f"Product with ID {pid} does not exist"
            )
        order_products.append(product.model_dump())

    full_order = {
        "id": updated.id,
        "products": order_products
    }

    ok = order_list.update(full_order)

    if not ok:
        raise HTTPException(status_code=404, detail="Order not found")

    return {"message": "Order updated", "order": full_order}

@app.delete("/orders/{order_id}", status_code=status.HTTP_200_OK)
def delete_order(order_id: int):
    # Intentar eliminar el pedido de la lista enlazada
    order_deleted = order_list.delete(order_id)
    
    # Si no se encontró el pedido, lanzar error 404
    if not order_deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Devolver mensaje de éxito
    return {"message": "Order deleted"}

@app.get("/orders", status_code=status.HTTP_200_OK)
def list_orders():
    # Devolver la lista de pedidos completa
    return {"orders": order_list.list_all()}