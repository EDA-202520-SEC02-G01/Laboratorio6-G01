from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1


def new_map(capacity, limit_factor):
    my_map = {
        "table": al.new_array_list(capacity, me.new_entry(None, None)),
        "size": 0,
        "capacity": capacity,
        "limit_factor": limit_factor,
        "current_factor": 0
    }
    return my_map

def get(my_map, key):
    index = mf.hash_value(my_map, key)
    lista = my_map["table"]["elements"][index]
    for entry in lista:
        if default_compare(key, entry) == 0:
            return me.get_value(entry)
    return None
    
def is_empty(my_map):
    if my_map["size"]==0:
        return True
    return False