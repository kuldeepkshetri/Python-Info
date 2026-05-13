'''Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
'''

h,m,s=map(int,input("Enter hours , minutes, seconds:").split(","))
print("Hours =",h)
print("Minutes =",m)
print("Seconds =",s)

T=(h*3600)+(m*60)+s
print("Total Seconds = ",T)