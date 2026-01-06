"""
-------------------------------------------------------
Assignment 10, Task 2
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-07-21"
-------------------------------------------------------
"""
from Sorts_List_linked import Sorts
from List_linked import List

lst = List()

lst.append(9999)
lst.append(1231231231)
lst.append(341)
lst.append(44120)
lst.append(11239)
lst.append(23)

Sorts.radix_sort(lst)

for i in lst:
    print(i)
