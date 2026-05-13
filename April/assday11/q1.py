'''
1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9
'''

a=int(input ("Input ="))
max=0

while a>0:
    s=a%10
    if s>max :
        max=s
    a=a//10
print(max)