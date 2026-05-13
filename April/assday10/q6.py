'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to **check whether a number is an Armstrong number using loops**.

Input: 153
Output: Armstrong


153,370,371,407
'''

a=int(input("Input ="))
b=a
arm=0
len=len(str(a))
while a>0:
    rem=a%10
    arm=rem*rem*rem + arm
    a=a//10
if b==arm:
    print("Armstrong")
else:
    print("Not Armstrong")

l=0
v=b

for i in range (b):
    rem=b%10
    l=rem**len+l
    b=b//10
if v==l:
    print("Armstrong")
else:
    print("Not Armstrong")