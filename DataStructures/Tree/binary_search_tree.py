from DataStructures.Tree import bst_node


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
