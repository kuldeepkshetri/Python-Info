'''
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75

---
'''

a=int(input("Total bill amount = "))
b=int(input("GST = "))
c=int(input("Service charge = "))
d=int(input("NUmber of friends = "))

g=(a*5)/100
s=(a*10)/100
sc=a+g+s
t=sc/d
print("Final Bill = ",sc)
print("Each Person Pays = ",t)
