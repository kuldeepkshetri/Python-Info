'''
7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
'''

a,b=map(int,input("Input :").split(","))
s=1
while b>0:
    s=s*a
    b-=1
print("Output : ",s)