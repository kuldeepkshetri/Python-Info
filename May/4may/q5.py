'''
5.
Tech Number Checker

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number
'''

n=int(input("Enter a number: "))
len=len(str(n))
l=len//2
if len%2==0:
    a=n//(10**l)
    print("First half =",a)
    b=n%(10**l)
    print("Second half =",b)
    sum=a+b
    print("Sum =",sum)
    s=sum**2
    print("Sqaure =",s)
    if s==n:
        print("Tech number")
    else :
        print("Not tech number")
else:
    print("enter even digit number")