#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dect = {}
    for i in a_dictionary:
        new_dect[i] = a_dictionary[i] * 2
    return new_dect
