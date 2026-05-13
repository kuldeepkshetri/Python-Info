'''
8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number
'''

a=int(input("Input :"))
b=a*a*a
rev=0
c=a
v=0
print(b)

while a>0:
    rem=b%10
    rev=rev*10+rem
    b=b//10
    a=a//10


while rev>0:
    rem=rev%10
    v=v*10+rem
    rev=rev//10
print(v)
    

if v==c:
    print("Trimorphic Number")
else :
    print("Not Trimorphic Number")