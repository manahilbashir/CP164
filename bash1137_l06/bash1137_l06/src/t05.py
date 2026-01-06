"""
-------------------------------------------------------
Lab 6, Task 5
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-15"
-------------------------------------------------------
"""
from List_linked import List

my_list = List()
my_list.append("red")
my_list.append("green")
my_list.append("blue")
my_list.append("yellow")

first_item = my_list.peek()
print("First item (peeked):", first_item)

removed_item = my_list.remove("green")
print("Removed item:", removed_item)
