"""
-------------------------------------------------------
Lab 3, Task 6
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq
from utilities import pq_to_array
from utilities import priority_queue_test

pq = Priority_Queue()
source = [5, 44, 333, 22, 1]
target = []

array_to_pq(pq, source)

for i in pq:
    print(i)

pq_to_array(pq, target)

print(target)

priority_queue_test(target)
