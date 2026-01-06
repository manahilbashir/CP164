"""
-------------------------------------------------------
Lab 6, Task 1
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-15"
-------------------------------------------------------
"""
from List_linked import List

playlist = List()

playlist.prepend("Bohemian Rhapsody - Queen")

playlist.append("Imagine - John Lennon")

playlist.insert(1, "Like a Rolling Stone - Bob Dylan")

for each in playlist:
    print(each)
