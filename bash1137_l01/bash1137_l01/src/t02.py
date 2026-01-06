"""
-------------------------------------------------------
Lab 1, Task 2
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-10"
-------------------------------------------------------
"""
from Movie import Movie

title = "Delamorte Dellamore"
year = 1994
director = "Michele Soavi"
rating = 7.2
genres = [3, 4, 5, 8]

my_movie = Movie(title, year, director, rating, genres)

genres_list = my_movie.genres_list_string()

print(genres_list)
