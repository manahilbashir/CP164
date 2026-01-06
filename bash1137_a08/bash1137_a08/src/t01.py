"""
-------------------------------------------------------
Assignment 8, Task 1
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-07-05"
-------------------------------------------------------
"""
from BST_linked import BST

tree = BST()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)

print(tree.is_vaild())
tree._root._right._value = 4
print(tree.is_vaild())

tree2 = BST()
for i in range(1, 7):
    tree2.insert(i)

print(tree.levelordeer())
tree.remove(1)
print(tree.levelorder())
