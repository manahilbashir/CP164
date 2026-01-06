"""
-------------------------------------------------------
Assignment 4, Task 4
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-01"
-------------------------------------------------------
"""
from Queue_array import Queue

source1 = Queue()
source2 = Queue()

source1.insert(5)
source1.insert(2)
source1.insert(6)
source1.insert(7)

source2.insert(3)
source2.insert(2)
source2.insert(1)

target = Queue()
target.combine(source1, source2)

print("source1:", source1._values)
print("source2:", source2._values)
print("target:", target._values)
