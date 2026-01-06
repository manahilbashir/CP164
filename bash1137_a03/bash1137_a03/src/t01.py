"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from Stack_array import Stack
from functions import stack_split_alt


def main():
    s = Stack()
    x = [0, 5, 2, 8, 6, 9]

    for v in x:
        s.push(v)
    target1, target2 = stack_split_alt(s)
    print(target1)
    print(target2)


main()
