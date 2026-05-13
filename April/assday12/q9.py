'''
9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
'''
a=int(input("Input :"))
di=len(str(a))
rev=0
sum=0
g=0
st=0
for i in range (di):
    rem=a%10
    if i!=0:
        c=rem-b
        c=abs(c)
        rev=rev*10+c
        sum=sum+c
        if c>g:
            g=c
    b=rem
    a=a//10
while rev>0:
    rem=rev%10
    st=st*10+rem
    rev=rev//10
print("Step Difference :",st)
print("Sum :",sum)
print("Largest Number :",g)
if st%di:
    print("Balanced")
else :
    print("Unbalanced")