'''
5.
Strong Number Detector

A banking security system uses Strong Numbers for special authentication testing.
The user enters a range of numbers.
The system identifies all Strong Numbers between the given range using nested loops.

A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

Example:
145

1! + 4! + 5!
= 1 + 24 + 120
= 145

Since the sum is equal to the original number, 145 is called a Strong Number.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Strong Numbers are:
1
2
145
'''

a=int(input("Enter starting number :"))
b=int(input("Enter ending number :"))
print("Strong Numbers are:")

for i in range (a,b+1):
    d=i
    sum=0
    while d>0:
        fact=1
        rem=d%10
        for j in range (rem,1,-1):
            fact=fact*j 
        sum=sum+fact
        d=d//10
    if i==sum:
        print(i)       