'''Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
'''


a=int(input("Amount:"))
b=a//100
c=a%100
d=c//50
e=(c%50)//10
print("₹100 x ",b)
print("₹50 x ",d)
print("₹10 x ",e)