'''
8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified
'''

a=int(input("Input :"))
rev=0
b=a

while a>0:
    rem=a%10
    rev=rev*10 + rem
    a=a//10 
c=rev-b
if c<0:
    c=c*-1

count =0

if c==0 :
    print("Reverse =",rev,end=" ")
    print("Difference = ",c,"Digits =",end=" ")
    print("1",end=" ")
    print("Perfect Match")


elif c%9==0:
    print("Reverse =",rev,end=" ")
    print("Difference = ",c,"Digits =",end=" ")
    while c>0:
        c=c//10
        count=count+1
    print(count,end=" ")
    print("Verified")

else :
    print("Reverse =",rev,end=" ")
    print("Difference = ",c,"Digits =",end=" ")
    while c>0:
        c=c//10
        count=count+1
    print(count,end=" ")
    print("Rejected")
