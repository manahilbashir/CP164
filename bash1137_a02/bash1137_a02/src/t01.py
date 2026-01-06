"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-17"
-------------------------------------------------------
"""
from Movie_utilities import get_by_year, read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

year = int(input("Enter a year: "))

ymovies = get_by_year(movies, year)

print("Movies in the year {}: ".format(year))

for movie in ymovies:
    print("==============================================")
    print(movie)
