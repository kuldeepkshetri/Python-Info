'''Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
'''

m=int(input("Total:"))
o=int(input("Obtained:"))

p=o/m*100

print(f"Percentage={p}%")