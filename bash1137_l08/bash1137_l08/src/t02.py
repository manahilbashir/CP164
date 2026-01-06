"""
-------------------------------------------------------
Lab 8, Task 2
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-06-25"
-------------------------------------------------------
"""
from morse import ByCode

code_a = ByCode('A', '.-')
code_b = ByCode('B', '-...')
code_c = ByCode('C', '-.-.')

print(f"Code for A: {str(code_a)}")
print(f"Code for B: {str(code_b)}")
print(f"Code for C: {str(code_c)}")

print(f"Is the Code for A equal to the Code for B? {'Yes' if code_a == code_b else 'No'}")
print(f"Does the Code for A come before the Code for B? {'Yes' if code_a < code_b else 'No'}")
print(f"Is the Code for A less than or equal to the Code for C? {'Yes' if code_a <= code_c else 'No'}")
