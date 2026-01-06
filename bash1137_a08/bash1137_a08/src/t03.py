"""
-------------------------------------------------------
Assignment 8, Task 2
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-07-05"
-------------------------------------------------------
"""

from functions import fill_bst, letter_table, do_comparisons, comparison_total
from BST_linked import BST


DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"


bst2 = BST()


fill_bst(bst2, DATA2)

fv = open("miserables.txt", "r", encoding="utf-8")
do_comparisons(fv, bst2)
t2 = comparison_total(bst2)

letter_table(bst2)
