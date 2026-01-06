"""
-------------------------------------------------------
Assingment 2, Task 2
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-17"
-------------------------------------------------------
"""
from Movie_utilities import get_by_rating, read_movies

file_handle = open('movies.txt', 'r')

movies = read_movies(file_handle)

rating = float(input("Enter a rating: "))

rmovies = get_by_rating(movies, rating)

print("Movies with a rating >= {}: ".format(rating))

for movie in rmovies:
    print("==============================================")
    print(movie)
