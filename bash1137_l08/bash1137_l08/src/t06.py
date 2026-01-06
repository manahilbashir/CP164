"""
-------------------------------------------------------
Lab 8, Task 6
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-28"
-------------------------------------------------------
"""
from BST_linked import BST
from morse import fill_code_bst, decode_morse, DATA1

bst = BST()

fill_code_bst(bst, DATA1)

morse_code = "... --- ..."
decoded_text = decode_morse(bst, morse_code)
print(f"Morse Code: {morse_code}")
print(f"Decoded Text in English: {decoded_text}")
