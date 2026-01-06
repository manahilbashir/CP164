"""
-------------------------------------------------------
Lab 4, Task 7
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-01"
-------------------------------------------------------
"""
from utilities import list_test
from Movie import Movie

fv = open('movies.txt', 'r')

source = fv.readlines()

list_test(source)
