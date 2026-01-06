"""
-------------------------------------------------------
Lab 4, Task 4
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-01"
-------------------------------------------------------
"""
from List_array import List

source = List()

source.append(3)
source.append(5)
source.insert(3, 6)

x = source.index(3)
print(x)

value = source.find(6)
print(value)

x = source.count(3)
print(x)

value = source.min()
print(value)

value = source.max()
print(value)
