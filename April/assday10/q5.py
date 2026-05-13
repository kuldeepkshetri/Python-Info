'''
5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to **check whether a given number is a palindrome using loops**.

Input: 121
Output: Palindrome
'''

i=int(input("Input ="))
a=i
rev=0
x=len(str(i))
y=i
while i>0:
    rem=i%10
    rev=rev*10+rem
    i=i//10
if a==rev:
    print("Palindrome")
else :
    print("Not Palindrome")

g=0
for d in range (1,x+1):
    rem=y%10
    g=g*10+rem
    y=y//10
if a==g:
    print("Palindrome")
else :
    print("Not Palindrome")