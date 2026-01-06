"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from functions import stack_reverse
from Stack_array import Stack

source_stack = Stack()

source_stack.push(8)
source_stack.push(1)
source_stack.push(9)

print(f"Stack before: {source_stack._values}")

stack_reverse(source_stack)

print(f"Stack after: ")

while not source_stack.is_empty():
    print(source_stack.pop())
