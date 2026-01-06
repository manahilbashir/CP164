"""
-------------------------------------------------------
Assignment 4, Task 5
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-01"
-------------------------------------------------------
"""
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
pq.insert(4)
pq.insert(6)
pq.insert(2)
pq.insert(8)

split_key = 3

higher_priority, lower_or_equal_priority = pq_split_key(pq, split_key)

print("Target 1 Queue:")
for value in higher_priority:
    print(value, end=' ')
print()

print("Target 2 Queue:")
for value in lower_or_equal_priority:
    print(value, end=' ')
print()
