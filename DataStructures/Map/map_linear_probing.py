from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail


def is_available(table, pos):

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


def put(my_map, key, value):
    valor=mf.hash_value(my_map,key)
    estado,pos=find_slot(my_map,key,valor)
    if not estado:
        my_map["table"]["elements"][pos]["key"]=key
        my_map["table"]["elements"][pos]["value"]=value
    my_map["table"]["current_factor"]+=1
    if my_map["table"]["current_factor"] > my_map["table"]["limit_factor"]:
        my_map=rehash(my_map)
    return my_map

def remove(my_map, key):
    pass
    
def contains(my_map, key): 
    lista = my_map['table']['elements']
    for llave in lista:
        if me.get_key(llave) == key:
            return True
    return False
    
def size(my_map):
    return my_map['table']['size']




def new_map(num_elements, load_factor, prime=109345121):
    capacity=(num_elements/load_factor)+1
    map={"prime":prime, "capacity":capacity,"scale":1,"shift":0,"table":{"size":capacity,"elements":[]},"current_factor":0,"limit_factor":load_factor,"size":0}
    for i in range(0,num_elements):
        
        map["table"]["elements"].append(me.new_map_entry(None, None))
    return map

def get(my_map, key):
    h=mf.hash_value(my_map,key)
    comp=find_slot(my_map,key,h)
    if comp[0]==True:
        return 
        