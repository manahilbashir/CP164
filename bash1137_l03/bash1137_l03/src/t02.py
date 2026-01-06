"""
-------------------------------------------------------
Lab 3, Task 2
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from Queue_array import Queue

q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)

value2 = q.peek()
value = q.remove()
value3 = q.peek()

print(value2)
print(value)
print(value3)
print("")

for i in q:
    print(i)
