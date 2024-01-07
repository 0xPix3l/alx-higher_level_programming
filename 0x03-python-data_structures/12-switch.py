#!/usr/bin/python3
a = 89
b = 10
tmp = 0
tmp = a     # tmp = 89
a = b
b = tmp
print("a={:d} - b={:d}".format(a, b))
