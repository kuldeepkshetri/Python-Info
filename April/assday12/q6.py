'''
6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number
'''

a=int(input("Input :"))
squ=a*a
g=a
rev=0
d=0
while a>0:
    rem=squ%10
    rev=rev*10+rem
    squ=squ//10
    a=a//10

while rev>0:
    rem=rev%10
    d=d*10+rem
    rev=rev//10


if g==d:
    print("Automatic Number ")
else:
    print("Not Automatic Number")




