"""
-------------------------------------------------------
Assignment 4, Task 6
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-01"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

for value in [30, 45, 60, 75, 90, 95]:
    pq.insert(value)

key = 40

higher_than_key, lower_or_equal_to_key = pq.split_key(key)

print("Original Priority Queue (should be empty):")
for value in pq:
    print(value, end=' ')
print()

print("Priority Queue with values higher than key:")
for value in higher_than_key:
    print(value, end=' ')
print()

print("Priority Queue with values lower than or equal to key:")
for value in lower_or_equal_to_key:
    print(value, end=' ')
print()
