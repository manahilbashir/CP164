"""
-------------------------------------------------------
Assingment 2, Task 3
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-17"
-------------------------------------------------------
"""
from Movie_utilities import get_by_genre, read_movies

file_handle = open("movies.txt", 'r')

movies = read_movies(file_handle)

genre = int(input("Enter a genre code: "))

gmovies = get_by_genre(movies, genre)

for movie in gmovies:
    print("========================================")
    print(movie)
