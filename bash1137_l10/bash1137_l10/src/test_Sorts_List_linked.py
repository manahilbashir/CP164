"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2024-07-13"
-------------------------------------------------------
"""
# Imports
import random

from random import randint
from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    for i in range(SIZE - 1, -1, -1):
        num = Number(i)
        values.insert(0, num)

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    for i in range(SIZE):
        num = Number(i)
        values.insert(0, num)

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """
    lists = []
    for i in range(TESTS):
        link = List()

        for j in range(SIZE):
            r = random.randint(0, XRANGE)
            num = Number(r)
            link.insert(0, num)

        lists.append(link)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    Number.comparisons = 0
    Sorts.swaps = 0
    s = create_sorted()
    func(s)
    sc = Number.comparisons
    ss = Sorts.swaps
    Number.comparisons = 0
    Sorts.swaps = 0
    r = create_reversed()
    func(r)
    rc = Number.comparisons
    rs = Sorts.swaps
    Number.comparisons = 0
    Sorts.swaps = 0
    d = create_randoms()
    for i in range(len(d)):
        func(d[i])
    dc = Number.comparisons // len(d)
    ds = Sorts.swaps // len(d)
    print(f'{title:14} {sc:8} {rc:8} {dc:8} {ss:8} {rs:8} {ds:8}')
    return


print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")
test_sort(SORTS[0][0], SORTS[0][1])
test_sort(SORTS[1][0], SORTS[1][1])
test_sort(SORTS[2][0], SORTS[2][1])
test_sort(SORTS[3][0], SORTS[3][1])
test_sort(SORTS[4][0], SORTS[4][1])
