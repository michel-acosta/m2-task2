# README: Proyecto FastAPI con árbol binario de búsqueda y lista enlazada simple

Este proyecto consiste en desarrollar una pequeña API en FastAPI que gestione productos y pedidos, utilizando como estructuras de datos:

* Un árbol binario de búsqueda (BST) para almacenar productos
* Una lista enlazada simple para almacenar pedidos

El objetivo de la tarea es practicar el manejo de estructuras de datos avanzadas y la creación de endpoints en FastAPI sin usar una base de datos.

Todos los ficheros del proyecto están comentados extensamente.

## Ficheros del proyecto

### main.py
Contiene todos los endpoints de la API.

### data/bst_products.py
Implementa el **árbol binario** donde se almacenan los productos.  
Funciones principales:

- Insertar producto.
- Buscar producto.
- Actualizar producto.
- Eliminar producto.
- Recorrer el árbol en orden para devolver los productos ordenados.

### data/linkedlist_orders.py
Contiene la **lista enlazada** que almacena pedidos.  
Funciones principales:

- Añadir un pedido.
- Buscar pedido.
- Actualizar pedido.
- Eliminar pedido.
- Devolver todos los pedidos.

### models/
Modelos Pydantic para poder validar los datos de entrada del usuario:
- `Product`
- `Order`

### PYTHON-TASK2.postman_collection.json
Fichero que se puede importar en Postman para probar la API

---

## Endpoints implementados

### **PARA PRODUCTOS**

#### POST /products

Crea un nuevo producto en el árbol binario.  

#### GET /products/{id}

Busca y devuelve un producto por id.

#### GET /products

Devuelve todos los productos ordenados por id.

#### PUT /products/{id}

Actualiza un producto existente.

#### DELETE /products/{id}

Elimina un producto del árbol binario.

### **PARA PEDIDOS**

#### POST /orders

Crea un nuevo pedido.

El usuario envía solamente los ids de los productos, e internamente los sustituimos por los productos completos del árbol.

#### GET /orders/{id}

Obtiene un pedido por su id.

#### GET /orders

Devuelve todos los pedidos almacenados en la lista enlazada.

#### PUT /orders/{id}

Actualiza un pedido.

#### DELETE /orders/{id}

Elimina un pedido.

## Estructuras de datos utilizadas

### Árbol Binario de Búsqueda (BST)

Lo utilizamos para almacenar productos de manera ordenada.

La parte más compleja ha sido la de eliminación, ya que hay que tener en cuenta que cuando el nodo no tiene hijos se puede borrar directamente, pero si tiene un hijo éste debe sustituir a su padre, y si tiene varios debemos quedarnos con el mínimo nodo del subárbol derecho.

### Lista enlazada

La usamos para almacenar los pedidos

Cada nodo contiene un diccionario con la información del pedido y un puntero al siguiente nodo

## Requerimientos

### Dependencias

`pip install fastapi uvicorn pydantic`

## Conclusiones y observaciones

La práctica me ha servido para entender cómo funcionan estructuras avanzadas como los árboles binarios y las listas enlazadas. También descubrí Pydantic, que en combinación con FastAPI facilita bastante la creación de endpoints y la validación de los datos.

La parte más complicada ha sido la implementación del borrado de nodos en el árbol, especialmente el caso de dos hijos.
