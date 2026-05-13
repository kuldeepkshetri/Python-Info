'''
Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000
'''


wage=int(input("Enter your daily wage:"))
day=int(input("Enter your days:"))
print(f"Daily wage ={wage} \nDays ={day}")
s=wage*day
print("Salary =",s)