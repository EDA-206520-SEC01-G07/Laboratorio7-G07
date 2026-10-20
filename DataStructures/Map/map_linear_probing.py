import random
import math
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as al

def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(math.ceil(num_elements / load_factor))

    return {
        "prime": prime,
        "capacity": capacity,
        "scale": random.randint(1, prime - 1),
        "shift": random.randint(0, prime - 1),
        "limit_factor": load_factor,
        "current_factor": 0,
        "size": 0,
        "table": {"elements": [{"key": None, "value": None} for _ in range(capacity)],
              "size": capacity},
    }

def put(my_map, key, value):
    hash_llave = mf.hash_value(my_map, key)
    occupied, first_avail = find_slot(my_map, key, hash_llave)

    if not occupied:
        my_entry = me.new_map_entry(key, value)
        my_map["table"]["elements"][first_avail] = my_entry
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    else:
        me.set_value(al.get_element(my_map["table"], first_avail), value)

    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)

    return my_map

def find_slot(my_map, key, hash_value):
    first_avail = None
    for _ in range(my_map["capacity"]):
        if is_avaible(my_map["table"], hash_value):
            if first_avail is None:
                first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
                return False, first_avail
        elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            return True, hash_value
        hash_value = (hash_value + 1) % my_map["capacity"]
    return False, first_avail


def is_avaible(table, pos):
    entry = al.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    return False

def default_compare(key, entry):
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1

def contains(my_map, key):
    hash_llave = mf.hash_value(my_map, key)
    occupied, _ = find_slot(my_map, key, hash_llave)
    return occupied

def get(my_map, key):
    hash_key = mf.hash_value(my_map, key)
    occupied, position = find_slot(my_map, key, hash_key)
    if occupied:
        return me.get_value(al.get_element(my_map["table"], position))
    return None

def remove(my_map, key):
    hash_key = mf.hash_value(my_map, key)
    occupied, position = find_slot(my_map, key, hash_key)
    if occupied:
        entry = al.get_element(my_map["table"], position)
        me.set_key(entry, "__EMPTY__")
        me.set_value(entry, "__EMPTY__")
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    return my_map

def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    return size(my_map) == 0

def key_set(my_map):
    respuesta = {
        "elements" : [],
        "size" : 0
    }
    for entry in my_map["table"]["elements"]:
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            al.add_last(respuesta, key)
    return respuesta
    

def value_set(my_map):
    respuesta = {
        "elements" : [],
        "size" : 0
    }
    
    for i in range(my_map["capacity"]):
        if not is_avaible(my_map["table"], i):
            entry = al.get_element(my_map["table"], i)
            al.add_last(respuesta, me.get_value(entry))
    return respuesta

def rehash(my_map):
    """
    Crea una tabla nueva con capacity = siguiente primo mayor al doble de la
    capacidad actual, y reinserta en ella las entradas vigentes.

    """
    nueva_tabla = new_map(2 * my_map["capacity"], 1, my_map["prime"])
    nueva_tabla["limit_factor"] = my_map["limit_factor"]

    for entry in my_map["table"]["elements"]:
        key = me.get_key(entry)
        value = me.get_value(entry)
        if key is not None and key != "__EMPTY__":
            nueva_tabla = put(nueva_tabla, key, value)

    my_map = nueva_tabla
    return my_map


def is_available(table, pos):
    return is_avaible(table, pos)
