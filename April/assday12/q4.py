'''
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''

a=int(input("Input :"))
sum=0
b=a
while a>0:
    rem =a%10
    fact=1
    for i in range (1,rem+1):
        fact=fact*i
    sum=sum+fact
    a=a//10
if sum==b:
    print("Strong Number")
else:
    print("Weak Number")