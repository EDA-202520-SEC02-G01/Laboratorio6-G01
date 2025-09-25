from DataStructures.List import array_list as al
import map_entry as me
import map_functions as mf

def contains(my_map, key): 
    lista = my_map['table']['elements']
    for llave in lista:
        if me.get_key(llave) == key:
            return True
    return False
    
def size(my_map):
    return my_map['table']['size']

