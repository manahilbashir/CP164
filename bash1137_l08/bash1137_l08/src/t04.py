"""
-------------------------------------------------------
Lab 8, Task 4
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-26"
-------------------------------------------------------
"""
from BST_linked import BST
from morse import fill_code_bst, DATA1

bst = BST()

fill_code_bst(bst, DATA1)

print(f"BST contends in order: ")
for each in bst.inorder():
    print(each)
