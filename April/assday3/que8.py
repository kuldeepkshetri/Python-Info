'''Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0
'''

M=int(input("MB = "))
G=M/1024
print("GB = ",G)