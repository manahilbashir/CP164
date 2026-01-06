"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-01"
-------------------------------------------------------
"""
from Queue_array import Queue

queue = Queue()

q1 = Queue()
q2 = Queue()

q1.insert(3)
q1.insert(4)
q1.insert(5)

q2.insert(7)
q2.insert(8)
q2.insert(9)

print(q1 == q2)

q2.insert(4)

print(q1 == q2)
