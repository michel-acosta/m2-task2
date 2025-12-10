# Importamos Optional para tipos que pueden ser nulos y List para tipar listas
from typing import Optional, List, Dict, Any

# Nodo de la lista enlazada, que contendrá un pedido
class OrderNode:
    def __init__(self, order: Dict[str, Any]):
        self.order = order  # Guardamos el objeto Order dentro del nodo
        self.next: Optional["OrderNode"] = None  # Enlace al siguiente nodo, que inicialmente será nulo

# Nuestra lista enlazada de pedidos
class OrderLinkedList:
    def __init__(self):
        self.head: Optional[OrderNode] = None  # La cabeza de la lista que al principio estará vacía

    # Añade un nuevo pedido en el punto inicial de la lista
    def add(self, order: Dict[str, Any]):
        new_node = OrderNode(order)  # Creamos el nuevo nodo
        new_node.next = self.head  # Colocamos la cabeza actual como siguiente de nuestro nodo
        self.head = new_node  # Colocamos nuestro nuevo nodo como cabeza de la lista

    # Busca un pedido por su id
    def get_by_id(self, order_id: int) -> Optional[Dict[str, Any]]:
        current = self.head  # Empezamos desde la cabeza de la lista

        while current: # Mientras current sea algo
            if current.order["id"] == order_id:  # Si encontramos el id, hemos encontrado el pedido...
                return current.order
            current = current.next  # ...si no, avanzamos al siguiente nodo

        return None  # Si no encontramos nada, devolvemos None

    # Actualiza un pedido existente por su id
    def update(self, updated_order: Dict[str, Any]):
        current = self.head # Empezamos desde la cabeza de la lista

        while current: # Mientras current sea algo
            if current.order["id"] == updated_order["id"]:  # Si encontramos el id, hemos encontrado el pedido...
                current.order = updated_order  # Reemplazamos el pedido por el nuevo
                return True  # Retornamos True para indicar que se actualizó
            current = current.next

        return False  # Retornamos False si no se encontró el pedido

    # Elimina un pedido por su id
    def delete(self, order_id: int):
        current = self.head # Empezamos desde la cabeza de la lista
        prev = None  # Nos guardamos el nodo anterior para poder actualizar el enlace

        while current: # Mientras current sea algo
            if current.order["id"] == order_id:  # Si encontramos el id, hemos encontrado el pedido...
                if prev: # Si ya hemos seteado el nodo previo...
                    prev.next = current.next  # ...saltamos el nodo actual (indicamos que el siguiente del previo es el siguiente del actual)
                else:
                    self.head = current.next  # Si prev es nada, estamos en la cabeza. Nos la saltamos
                return True  # Retornamos True para indicar que se eliminó
            prev = current  # Indicamos que nuestro nodo previo ahora será el nodo actual
            current = current.next  # Avanzamos al nodo siguiente

        return False  # Retornamos False si no se encontró el pedido

    # Devuelve una lista con todos los pedidos
    def list_all(self) -> List[Dict[str, Any]]:
        result = []  # Lista donde guardaremos todos los pedidos
        current = self.head # Empezamos desde la cabeza de la lista

        while current: # Mientras current sea algo
            result.append(current.order)  # Añadimos el pedido actual a la lista
            current = current.next  # Avanzamos al siguiente nodo

        return result # Devolvemos la lista

# Creamos una instancia de la lista enlazada
order_list = OrderLinkedList()