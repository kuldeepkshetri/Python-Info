'''
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15
'''
a=int(input("Input = "))
sum=1

for i in range (1,a+1):
    if i%2!=0:
        sum=sum*i
print("Output :",sum)