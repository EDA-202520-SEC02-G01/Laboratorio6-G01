from DataStructures.List import array_list as al
from  DataStructures.Map import map_entry as me
from  DataStructures.Map import map_functions as mf

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
        