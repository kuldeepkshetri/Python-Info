'''Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
'''

a=int(input("Amount: "))
d=(a*10)//100
print("Discount:",d)
f=a-d
print("Fianl =",f)
