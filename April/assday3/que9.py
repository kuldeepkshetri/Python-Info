'''Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
'''

d=int(input("Distance:"))
m=int(input("Mileage:"))
p=int(input("Petrol Price:"))
 
c=(d//m)*p
print("Cost=",c)