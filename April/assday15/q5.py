'''
5.  Automorphic Number Lock

A high-security digital locker validates access codes using a special mathematical rule.

When a user enters a numeric code, the system squares the number and checks whether the last digits of the square match the original number.
 If it matches, the code is considered valid.

An Automorphic Number is a number whose square ends with the same number.

Task:
Write a Python program to check whether a given number is an Automorphic Number or not.

Example:
Input:
25

Output:
Automorphic Number
'''

a=int(input("Input :"))
b=a*a
c=len(str(a))
r=0
i=0
v=0

while i<c:
    rem=b%10
    r=r*10+rem
    b=b//10
    i=i+1


while r>0:
    rem=r%10
    v=v*10+rem
    r=r//10

if v==a:
    print("Automorphic Number")
else :
    print("Not Automorphic Number")    
    
