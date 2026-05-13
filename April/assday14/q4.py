'''
4.Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code
'''

a=input("Input :")
b=int(a)

for i in a:
    rem=b%10
    c=0
    for x in a :
        if rem==int(x):
            c=c+1
    if c>=2:
        print("Invalid")
        break
    b=b//10
else :
    print("Valid Unique Code")
    