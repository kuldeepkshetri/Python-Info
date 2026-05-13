'''

4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number
'''

a=int(input("Input :"))
sum=0
pro=1
 
while a>0:
    rem=a%10
    sum=sum+rem
    pro=pro*rem
    a=a//10
if sum==pro:
    print("Spy Number")
else :
    print("Not Spy Number")
