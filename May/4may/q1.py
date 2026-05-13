'''
1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern
'''
a=int(input("Input :"))
rev=0

while a>0:
    rem=a%10
    rev=rev*10+rem
    a=a//10

b=rev%10
rev=rev//10
print("Differences :",end=" ")
count=0
max=0
g=""

while rev>0:
    rem=rev%10
    dif=abs(b-rem)
    b=rem
    print(dif,end=" ")
    rev=rev//10
    if dif%2==0:
        count=count+1
    if max<dif:
        max=dif
    g=g+str(dif)

print("\nEven Differences Count =",count)
print("Max Difference =",max)

f=g[0]

for i in g:
    if i!=f:
        print("Non Uniform Pattern ")
        break
else :
    print("Uniform Pattern") 