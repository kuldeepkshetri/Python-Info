'''
1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime
'''
a=int(input("Input :"))
sum=0
rev=0
d=a
while a>0:
    rem=a%10
    sum=sum+rem
    rev=rev*10+rem
    a=a//10
print("Sum of Digits =",sum)
print("Reverse =",rev)
e=abs(d-rev)
print("Difference =",e)
c=e+sum
print("Final Result =",c)

for i in range (2,c//2+1):
    if c%i==0:
        print("Not Prime")
        break
else :
    print("Prime NUmber")
