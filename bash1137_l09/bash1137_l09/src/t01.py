"""
-------------------------------------------------------
Lab 9, Task 1
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-07-04"
-------------------------------------------------------
"""
from functions import hash_table
from Movie_utilities import read_movies

fh = open('movies.txt', 'r')
movies = read_movies(fh)
print("Hashes")
hash_table(7, movies)
