'''Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
'''

p=int(input("Cost Price = "))
s=int(input("Selling Price ="))

a=s-p
v=a/p*100
print("Profit = ",a)
print("Profit % =",v)

