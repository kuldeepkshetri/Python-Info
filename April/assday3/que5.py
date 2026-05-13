'''Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
'''

a,b,c=map(int,input("Enter the marks of three subject :").split())
print(f"Marks = {a},{b},{c}")
ave=(a+b+c)/3
print("Average =",ave)