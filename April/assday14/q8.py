'''
8.
 ATM Note Counter

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7
'''

a=int(input("Input :"))
b=a
x=0

for i in range (100,a+1,100):
    c=a-100
    if True:
        x=x+1
print("Notes =",x)