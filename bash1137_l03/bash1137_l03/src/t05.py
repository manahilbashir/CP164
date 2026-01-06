"""
-------------------------------------------------------
Lab 3, Task 5
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

list = [5, 4, 3, 2, 1]

for i in list:

    pq.insert(i)

value = pq.remove()

print(value)
print("")

for i in pq:
    print(i)
