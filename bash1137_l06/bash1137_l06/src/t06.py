"""
-------------------------------------------------------
Lab 6, Task 6
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-15"
-------------------------------------------------------
"""
from List_linked import List

my_list = List()
my_list.append("apple")
my_list.append("banana")
my_list.append("cherry")

item_at_index_1 = my_list[1]
print("Item at index 1:", item_at_index_1)

my_list[1] = "blueberry"
print("New item at index 1:", my_list[1])
