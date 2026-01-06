"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-17"
-------------------------------------------------------
"""
from Movie_utilities import genre_counts, read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

counts = genre_counts(movies)

print("Counts: {}".format(counts))
