from typing import Optional  # Para poder usar tipos que pueden ser None
from models.product import Product  # Importamos el modelo Product que define nuestros productos

# Nodo del árbol binario, que contendrá un producto
class ProductNode:
    def __init__(self, product: Product):
        self.product = product  # Guardamos el producto dentro del nodo
        self.left: Optional["ProductNode"] = None  # Hijo izquierdo, inicialmente None
        self.right: Optional["ProductNode"] = None  # Hijo derecho, inicialmente None

# Árbol binario de búsqueda para productos
class ProductBST:

    def __init__(self):
        self.root: Optional[ProductNode] = None  # Raíz del árbol, inicialmente vacía

    # Inserta un nuevo producto en el árbol
    def insert(self, product: Product):
        if not self.root:  # Si el árbol está vacío
            self.root = ProductNode(product)  # El nuevo nodo se convierte en la raíz
            return

        current = self.root # Arrancamos desde la raíz
        while True:
            if product.id < current.product.id:  # Si el id del producto es menor que el nodo actual...
                if current.left is None:  # Si no hay hijo izquierdo...
                    current.left = ProductNode(product)  # ...insertamos el nodo a la izquierda
                    return
                current = current.left  # Avanzamos al hijo izquierdo
            else:  # Si el id del producto es mayor o igual que el nodo actual...
                if current.right is None:  # Si no hay hijo derecho...
                    current.right = ProductNode(product)  # ...insertamos el nodo a la derecha
                    return
                current = current.right  # Avanzamos al hijo derecho

    # Busca un producto por su id
    def search(self, product_id: int) -> Optional[Product]:
        node = self._find_node(product_id) # Buscamos el nodo con nuestra función auxiliar
        if not node:
            return None # Si no existe, devolvemos none
        
        return node.product # Si existe, devolvemos el producto de ese nodo

    # Actualiza un producto existente
    def update(self, product: Product):
        node = self._find_node(product.id) # Buscamos el nodo con nuestra función auxiliar
        if node:
            node.product = product # Reemplazamos el producto del nodo
            return True
        return False

    # Elimina un producto por su id
    def delete(self, product_id: int):    

        # Definimos una función recursiva para eliminar el nodo
        def delete_rec(node, product_id):
            
            if node is None: # Si el nodo es None, no se encontró
                return None, False
            
            if product_id < node.product.id: # Si el id es menor, continuamos por la izquierda del árbol
                node.left, deleted = delete_rec(node.left, product_id) 
                # recibimos una tupla con el subárbol izquierdo actualizado y un booleano indicando si se ha eliminado o no
                return node, deleted
            
            elif product_id > node.product.id: # Si el id es mayor, continuar por la derecha
                node.right, deleted = delete_rec(node.right, product_id)
                # recibimos una tupla con el subárbol derecho actualizado y un booleano indicando si se ha eliminado o no
                return node, deleted

            # Hemos encontrado el nodo a eliminar
            else:
                # No tiene hijos, eliminar directamente
                if node.left is None and node.right is None:
                    return None, True

                # Solo un hijo por la derecha, reemplazar por el hijo derecho
                if node.left is None:
                    return node.right, True

                # Solo un hijo por la izquierda, reemplazar por el hijo izquierdo
                if node.right is None:
                    return node.left, True

                # Tiene dos hijos, buscamos el sucesor más pequeño de su subárbol derecho                
                successor = node.right
                while successor.left:
                    successor = successor.left

                # Reemplazar el producto del nodo por el del sucesor
                node.product = successor.product

                # Eliminar el sucesor recursivamente
                node.right, deleted = delete_rec(node.right, successor.product.id)

                return node, deleted

        # Llamamos a la función recursiva empezando por root
        self.root, deleted = delete_rec(self.root, product_id)

        return deleted

# Métodos auxiliares privados

    # Busca un nodo en el árbol por su id
    def _find_node(self, product_id: int):    
        current = self.root # Arrancamos desde la raíz

        while current:
            if product_id == current.product.id:  # Si encontramos el nodo, lo devolvemos
                return current
            elif product_id < current.product.id: # Si el id buscado es menor...
                current = current.left # ...vamos al hijo izquierdo
            else: # Si el id buscado es mayor...
                current = current.right # ...vamos al hijo derecho

        return None # Si no se encuentra, devolvemos None

# Creamos una instancia del BST
product_tree = ProductBST()