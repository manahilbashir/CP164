"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-01"
-------------------------------------------------------
"""
from functions import Queue, queue_combine

source1 = Queue()
source2 = Queue()

source1.insert(8)
source1.insert(9)
source1.insert(6)
source1.insert(4)

source2.insert(3)
source2.insert(8)
source2.insert(3)

target = queue_combine(source1, source2)

source1_contents = []
while not source1.is_empty():
    source1_contents.append(source1.remove())

source2_contents = []
while not source2.is_empty():
    source2_contents.append(source2.remove())

target_contents = []
while not target.is_empty():
    target_contents.append(target.remove())

print("Source1:", source1_contents)  # Should be empty
print("Source2:", source2_contents)  # Should be empty
print("Target:", target_contents)    #
