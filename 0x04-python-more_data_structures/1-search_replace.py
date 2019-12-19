#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list
    ind = new.index(search)
    del new[ind]
    new.insert(ind, replace) 
    return new
