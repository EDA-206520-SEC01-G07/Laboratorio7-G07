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

def keys(my_bst, key_initial, key_final):
    list_key = sll.new_list()
    return keys_range(my_bst['root'], key_initial, key_final, list_key)

def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return list_key
    key = bst_node.get_key(root)
    if key_initial < key:
        keys_range(root['left'], key_initial, key_final, list_key)
    if key_initial <= key <= key_final:
        sll.add_last(list_key, key)
    if key_final > key:
        keys_range(root['right'], key_initial, key_final, list_key)
    return list_key

def remove(my_bst, key):
    my_bst['root'] = remove_node(my_bst['root'], key)
    return my_bst

def delete_min_tree(root):
    if root is None:
        return None
    if root['left'] is None:
        return root['right']
    root['left'] = delete_min_tree(root['left'])
    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root

def remove_node(root, key):
    if root is None:
        return None
    comparison = default_compare(key, root)
    if comparison == -1:
        root['left'] = remove_node(root['left'], key)
    elif comparison == 1:
        root['right'] = remove_node(root['right'], key)
    else:
        if root['right'] is None:
            return root['left']
        if root['left'] is None:
            return root['right']
        old = root
        root = get_min_node(old['right'])
        root['right'] = delete_min_tree(old['right'])
        root['left'] = old['left']
    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root

def floor(my_bst, key):
    node = floor_key(my_bst['root'], key)
    if node is None:
        return None
    return bst_node.get_key(node)

def floor_key(root, key):
    if root is None:
        return None
    comparison = default_compare(key, root)
    if comparison == 0:
        return root
    if comparison == -1:
        return floor_key(root['left'], key)
    candidate = floor_key(root['right'], key)
    if candidate is not None:
        return candidate
    return root

def ceiling(my_bst, key):
    node = ceiling_key(my_bst['root'], key)
    if node is None:
        return None
    return bst_node.get_key(node)

def ceiling_key(root, key):
    if root is None:
        return None
    comparison = default_compare(key, root)
    if comparison == 0:
        return root
    if comparison == 1:
        return ceiling_key(root['right'], key)
    candidate = ceiling_key(root['left'], key)
    if candidate is not None:
        return candidate
    return root

def select(my_bst, pos):
    if pos < 0 or pos >= size(my_bst):
        return None
    node = select_key(my_bst['root'], pos)
    if node is None:
        return None
    return bst_node.get_key(node)

def select_key(root, pos):
    if root is None:
        return None
    left_size = size_tree(root['left'])
    if pos < left_size:
        return select_key(root['left'], pos)
    if pos > left_size:
        return select_key(root['right'], pos - left_size - 1)
    return root

def rank(my_bst, key):
    return rank_keys(my_bst['root'], key)

def rank_keys(root, key):
    if root is None:
        return 0
    comparison = default_compare(key, root)
    if comparison == -1:
        return rank_keys(root['left'], key)
    if comparison == 1:
        return 1 + size_tree(root['left']) + rank_keys(root['right'], key)
    return size_tree(root['left'])

def key_set_tree(root, key_list):
    """Construye una lista con las llaves del subárbol, recorriéndolo en inorder
    (hijo izquierdo, raíz, hijo derecho), por lo que quedan de menor a mayor.
 
    Args:
        root (bst_node): Raíz del subárbol a examinar.
        key_list (single_linked_list): Lista de respuesta, que se llena en el recorrido.
 
    Returns:
        single_linked_list: Lista con las llaves del subárbol.
    """
    if root is not None:
        key_set_tree(root['left'], key_list)
        sll.add_last(key_list, bst_node.get_key(root))
        key_set_tree(root['right'], key_list)
    return key_list

def key_set(my_bst):
    """Retorna una lista con todas las llaves de la tabla, ordenadas de menor a mayor.
 
    Args:
        my_bst (binary_search_tree): El árbol de búsqueda.
 
    Returns:
        single_linked_list: Lista con todas las llaves de la tabla.
    """
    key_list = sll.new_list()
    return key_set_tree(my_bst['root'], key_list)

def value_set_tree(root, value_list):
    """Construye una lista con los valores del subárbol, recorriéndolo en inorder
    (hijo izquierdo, raíz, hijo derecho), en el orden de sus llaves.
 
    Args:
        root (bst_node): Raíz del subárbol a examinar.
        value_list (single_linked_list): Lista de respuesta, que se llena en el recorrido.
 
    Returns:
        single_linked_list: Lista con los valores del subárbol.
    """
    if root is not None:
        value_set_tree(root['left'], value_list)
        sll.add_last(value_list, bst_node.get_value(root))
        value_set_tree(root['right'], value_list)
    return value_list

def value_set(my_bst):
    """Retorna una lista con todos los valores de la tabla, en el orden de sus llaves.
 
    Args:
        my_bst (binary_search_tree): El árbol de búsqueda.
 
    Returns:
        single_linked_list: Lista con todos los valores de la tabla.
    """
    value_list = sll.new_list()
    return value_set_tree(my_bst['root'], value_list)

def height_tree(root):
    """Retorna la altura del subárbol que empieza en root.
 
    La altura de un árbol vacío es 0, la de un solo nodo es 1, y en general es
    1 + la mayor de las alturas de sus dos hijos. Cada llamada retorna su altura
    a la llamada que la hizo, por lo que no se necesita un contador externo.
 
    Args:
        root (bst_node): Raíz del subárbol a examinar.
 
    Returns:
        int: Altura del subárbol.
    """
    if root is None:
        return 0
    left_height = height_tree(root['left'])
    right_height = height_tree(root['right'])
    if left_height > right_height:
        return 1 + left_height
    return 1 + right_height

def height(my_bst):
    """Retorna la altura del árbol de búsqueda.
 
    Args:
        my_bst (binary_search_tree): El árbol de búsqueda.
 
    Returns:
        int: Altura del árbol.
    """
    return height_tree(my_bst['root'])
