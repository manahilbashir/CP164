"""
-------------------------------------------------------
Lab 3, Task 4
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

value = [1, 2, 3, 4, 5]

for i in value:
    pq.insert(i)

x = pq.peek()
print(x)
print("")

for i in pq:
    print(i)
