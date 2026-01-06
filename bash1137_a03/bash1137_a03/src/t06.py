"""
-------------------------------------------------------
Assignment 3, Task 6
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from Stack_array import Stack
from functions import reroute

opstring = "SSXSX"
values_in = [1, 2, 3, 4, 5]
values_out = reroute(opstring, values_in)
print(values_out)
