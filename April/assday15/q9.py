'''
9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number
'''

a=int(input("Input :"))
i=1
sum=0

while i<=a//2:
    rem=a%i
    if rem==0:
        sum=sum+i
    i=i+1

if sum>a:
    print("Abundant Number")
else :
    print("Not Abumdant Number")