'''
5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number
'''

a=int(input("Input :"))
s=9


while a>0:
    rem=a%10
    if rem<=s:
        s=rem
    else :
        print("Not Stable")
        break
    a=a//10
else:
    print("Stable Number")