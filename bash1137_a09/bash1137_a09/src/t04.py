"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-07-14"
-------------------------------------------------------
"""
from BST_linked import BST

bst = BST()

bst.insert(1)
bst.insert(21)
bst.insert(321)
bst.insert(4321)
bst.insert(54321)
bst.insert(6542321)

one, two, three = bst.node_counts()

print(one)
print(two)
print(three)

print(321 in bst)

val = bst.parent(20)

val2 = bst.parent_r(20)

print(val, val2)
