'''
Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5

'''

a=int(input("Monthly Salary ="))
b=int(input("Working days ="))
c=int(input("Working hours per day ="))

d=a/b
e=a/(c*b)
print("Salary per day =",d)
print("Salary per hour =",e)