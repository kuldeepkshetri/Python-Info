'''
4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
'''
a=int(input("Enter starting number :"))
b=int(input("Enter ending number :"))

for i in range (a,b+1):
    b=len(str(i))
    d=i
    c=0
    while d>0:
        rem=d%10
        c=rem**b+c
        d=d//10
    if i==c:
        print(i)