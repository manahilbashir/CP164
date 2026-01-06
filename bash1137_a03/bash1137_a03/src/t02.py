"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from Stack_array import Stack


def main():
    s = Stack()
    x = [1, 2, 3, 4, 5, 6]
    for v in x:
        s.push(v)

    target1, target2 = s.split_alt()

    print(target1)
    print(target2)


main()
