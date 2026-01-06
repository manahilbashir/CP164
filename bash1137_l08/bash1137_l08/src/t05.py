"""
-------------------------------------------------------
Lab 8, Task 5
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-28"
-------------------------------------------------------
"""
from BST_linked import BST
from morse import fill_letter_bst, encode_morse, DATA1

bst = BST()

fill_letter_bst(bst, DATA1)

text = "MY NAME IS DAVID BROWN"
morse_code = encode_morse(bst, text)
print(f"Original Text: {text}")
print(f"Encoded Morse Code: {morse_code}")
