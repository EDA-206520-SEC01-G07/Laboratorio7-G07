from DataStructures.Tree import bst_node
from DataStructures.List import single_linked_list as sll

def new_map():
    """Crea una nueva tabla de simbolos (map) ordenada basada en un árbol binario de búsqueda (BST).

    Returns:
        tabla de simbolos creada, con root inicialmente en None
    """
    my_bst = {'root': None}
    return my_bst


def default_compare(key, element) -> int:
    """Compara una llave con la llave de un nodo.

    Args:
        key (Any): Llave a comparar.
        element (bst_node): Nodo contra el que se compara.

    Returns:
        int: 0 si son iguales, 1 si key es mayor, -1 si key es menor.
    """
    element_key = bst_node.get_key(element)
    if key == element_key:
        return 0
    elif key > element_key:
        return 1
    return -1


def size(my_bst):
    """Retorna el número de entradas en la tabla de simbolos.

    Args:
        my_bst (binary_search_tree): El árbol de búsqueda.

    Returns:
        int: El número de elementos en la tabla.
    """
    return size_tree(my_bst['root'])


def size_tree(root):
    """Retorna el tamaño del subárbol que empieza en root (0 si es None)."""
    if root is None:
        return 0
    return root['size']


def insert_node(root, key, value):
    """Inserta (o actualiza) la pareja llave-valor en el subárbol y retorna su raíz."""
    if root is None:
        return bst_node.new_node(key, value)

    comparison = default_compare(key, root)
    if comparison == 1:
        root['right'] = insert_node(root['right'], key, value)
    elif comparison == -1:
        root['left'] = insert_node(root['left'], key, value)
    else:
        root['value'] = value

    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root

def put(my_bst, key, value):
    root = insert_node(my_bst['root'], key, value)
    my_bst['root'] = root
    return my_bst

def get_node(root, key):
    """Obtiene el nodo con la key buscada si está vacia la rama retorna None, retorna el nodo en el que se encuentra la key."""
    if root is None:
        return None
    comparison = default_compare(key, root)
    if comparison == 1:
        root = root['right']
        result = get_node(root, key)
    elif comparison == -1:
        root = root['left']
        result = get_node(root, key)
    else:
        return root
    return result

def get(my_bst, key):
    """Obtiene el valor asociado a la key buscada en el binary search tree, en caso de no existir la llave retorna None."""
    node = get_node(my_bst['root'], key)
    if node is None:
        return None
    return bst_node.get_value(node)

def contains(my_bst, key):
    node = get_node(my_bst['root'], key)
    return node is not None

def is_empty(my_bst):
    if size(my_bst) == 0:
        return True
    return False

def get_min_node(root):
    if root is None:
        return None
    if root['left'] is None:
        return root
    else:
        root = root['left']
        result = get_min_node(root)
    return result

def get_min(my_bst):
    node = get_min_node(my_bst['root'])
    if node is None:
        return None
    return node['key']

def get_max_node(root):
    if root is None:
        return None
    if root['right'] is None:
        return root
    else:
        root = root['right']
        result = get_max_node(root)
    return result

def get_max(my_bst):
    node = get_max_node(my_bst['root'])
    if node is None:
        return None
    return node['key']

def delete_min_tree(root):
    """Elimina el nodo con la llave más pequeña del subárbol y retorna la nueva raíz.
 
    Args:
        root (bst_node): Raíz del subárbol a examinar.
 
    Returns:
        bst_node: Raíz del subárbol sin la llave más pequeña (None si queda vacío).
    """
    if root is None:
        return None
    if root['left'] is None:
        return root['right']
    root['left'] = delete_min_tree(root['left'])
    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root

def delete_min(my_bst):
    """Elimina la llave más pequeña de la tabla y su valor asociado.
 
    Args:
        my_bst (binary_search_tree): El árbol de búsqueda.
 
    Returns:
        binary_search_tree: El árbol sin la llave más pequeña.
    """
    my_bst['root'] = delete_min_tree(my_bst['root'])
    return my_bst

def delete_max_tree(root):
    """Elimina el nodo con la llave más grande del subárbol y retorna la nueva raíz.
    
    Args:
        root (bst_node): Raíz del subárbol a examinar.
 
    Returns:
        bst_node: Raíz del subárbol sin la llave más grande (None si queda vacío).
    """
    if root is None:
        return None
    if root['right'] is None:
        return root['left']
    root['right'] = delete_max_tree(root['right'])
    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root
 
 
def delete_max(my_bst):
    """Elimina la llave más grande de la tabla y su valor asociado.
 
    Args:
        my_bst (binary_search_tree): El árbol de búsqueda.
 
    Returns:
        binary_search_tree: El árbol sin la llave más grande.
    """
    my_bst['root'] = delete_max_tree(my_bst['root'])
    return my_bst

def values_range(root, key_initial, key_final, list_value):
    if root is None:
        return list_value
    key = bst_node.get_key(root)
    if key_initial < key:
        values_range(root['left'], key_initial, key_final, list_value)
    if key_initial <= key <= key_final:
        sll.add_last(list_value, bst_node.get_value(root))
    if key_final > key:
        values_range(root['right'], key_initial, key_final, list_value)
    return list_value

def values(my_bst, key_initial, key_final):
    list_value = sll.new_list()
    return values_range(my_bst['root'], key_initial, key_final, list_value)