"""
-------------------------------------------------------
Task 2
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-10"
-------------------------------------------------------
"""
from functions import file_analyze

with open("example.txt", "w") as file:
    file.write("Hello World!\n")
    file.write("12345\n")
    file.write("This is a test.\n")
    file.write("    \n")

with open("example.txt", "r") as file:
    upper_count, lower_count, digit_count, whitespace_count, remaining_count = file_analyze(
        file)
    print("Uppercase:", upper_count)
    print("Lowercase:", lower_count)
    print("Digits:", digit_count)
    print("Whitespace:", whitespace_count)
    print("Remaining:", remaining_count)
