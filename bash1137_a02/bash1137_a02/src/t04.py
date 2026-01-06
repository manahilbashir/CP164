"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-17"
-------------------------------------------------------
"""
from Movie_utilities import get_by_genres, read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

genres = []

user_input = int(input("Enter a genre code (-1 TO QUIT): "))
while user_input != -1:
    genres.append(user_input)
    user_input = int(input("Enter a genre code (-1 TO QUIT): "))

gmovies = get_by_genres(movies, genres)

for movie in gmovies:
    print("===========================================")
    print(movie)
