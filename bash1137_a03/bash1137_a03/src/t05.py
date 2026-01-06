"""
-------------------------------------------------------
Assignment 3, Task 5
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from Stack_array import Stack
from functions import postfix

test_expressions = [
    "10 5 -",
    "1 2 + 20 * 3 7 * -",
    "8 9 + 5 /"
]

for expr in test_expressions:
    result = postfix(expr)
    print(f"{expr} evaluates to {result}")
