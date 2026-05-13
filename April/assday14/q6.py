'''
6.
Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29
'''

a=int(input("Input :"))

while True:
    a=a+1
    for i in range (2,a//2+1):
        if a%i==0 :
            print(a)
            break
    else :
        print("Prime Cabin =",a)
        break