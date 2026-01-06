"""
-------------------------------------------------------
Lab 8, Task 1
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-25"
-------------------------------------------------------
"""
from morse import ByLetter

letter_a = ByLetter('A', '.-')
letter_b = ByLetter('B', '-...')
letter_c = ByLetter('C', '-.-.')

print(f"Letter A: {str(letter_a)}")
print(f"Letter B: {str(letter_b)}")
print(f"Letter C: {str(letter_c)}")

aisb = "Yes" if letter_a == letter_b else "No"

abeforeb = "Yes" if letter_a < letter_b else "No"

aandc = "Yes" if letter_a <= letter_c else "No"

print(f"Is Letter A equal to Letter B? {aisb}")
print(f"Is Letter A come before Letter B? {abeforeb}")
print(f"Is Letter A less than or equal to Letter C? {aandc}")
