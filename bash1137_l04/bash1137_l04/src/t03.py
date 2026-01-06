"""
-------------------------------------------------------
Lab 4, Task 3
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-01"
-------------------------------------------------------
"""
from List_array import List

source = List()

source.append(6)
source.append(7)
source.append(8)
source.insert(8, 9)
x = source.remove(8)

print(x)
for i in source:
    print(i)
