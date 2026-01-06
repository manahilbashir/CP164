"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from Stack_array import Stack

source_stack = Stack()

source_stack._values.extend([7, 6, 4])

print(f"Stack before: {source_stack._values}")

source_stack.reverse()

print(f"Stack after: {source_stack._values}")
