'''
4. Numbers Divisible by 3 Between Two Numbers
A school is organizing a quiz competition. Only students whose roll numbers are divisible by 3 are selected for the first round. The teacher enters a roll number range and wants the system to display eligible roll numbers.
Write a program to display numbers divisible by 3 between two given numbers using loops.

Input:
10 25

Output:
12 15 18 21 24
'''

a,b=map(int,input("Input :").split(","))

if a%3==0:
    while a<=b:
        print(a)
        a=a+3
elif a%3==1:
    a=a+2
    while a<=b :
        print(a)
        a=a+3
else :
    a=a+1
    while a<=b:
        print(a)
        a=a+3

    