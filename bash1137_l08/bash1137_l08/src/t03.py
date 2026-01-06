"""
-------------------------------------------------------
Lab 8, Task 3
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-26"
-------------------------------------------------------
"""
from BST_linked import BST
from morse import fill_letter_bst, DATA1

bst = BST()

fill_letter_bst(bst, DATA1)

for each in bst.inorder():
    print(each)
