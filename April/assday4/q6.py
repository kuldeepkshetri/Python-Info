'''Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0
'''


a=int(input("Data = "))
b=a*1024
c=b*1024
print("In MB =",b)
print("In KB =",c)