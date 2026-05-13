'''
1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number
'''

a=int(input("Input ="))
low=99
b=0
i=0
sum=0
rev=0
digit=len(str(a))

while a>0:
    rem=a%10
    rev=rev*10+rem
    a=a//10

print("Products :",end=" ")
while rev>0:
    rem=rev%10
    c=rem*b
    if i>0: 
        print(c ,end=" ")
    b=rem
    rev=rev//10
    i=i+1
    sum=sum+c
    if c<low and c!=0:
        low=c
print("\nSum =",sum)
print("Smallest =",low)
    
if sum%digit==0:
    print("Stable NUmber ")
else :
    print("Unstable Number ")