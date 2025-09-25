from DataStructures.List import array_list as al
import map_entry as me
import map_functions as mf

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail


def is_available(table, pos):

   entry = lt.get_element(table, pos)
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
    

