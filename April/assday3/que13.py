'''Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0

'''

a=int(input("Principal ="))
b=int(input("Rate ="))
c=int(input("Time ="))

e= a *(1+b/100)**c
print("Amount = ",e)
print("Compound Interest = ",e-a)
