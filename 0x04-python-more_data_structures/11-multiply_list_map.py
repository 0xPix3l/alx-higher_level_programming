#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    a = lambda i : i * number
    y = list(map(a, my_list))   # map(func, list) and list is for adding this into new list
    return y
