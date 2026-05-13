'''
5.
Calendar System – Leap Year Checker
A digital calendar system needs to check whether a year is a leap year.
A year is a leap year if:

It is divisible by 400, OR
It is divisible by 4 but not by 100
Write a program using inline if to display whether the year is a leap year or not.
'''

a=int(input("Year :"))

print("Year is ","leap year " if (a%400==0) or (a%4==0 and a%100!=0) else "not leap year " )