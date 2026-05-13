'''
2. Digit Sum Mirror Checker

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number
'''

a=int(input("Input :"))
l=len(str(a))
sum=0
b=str(a)


count=0
sum2=0
for j in b:
    c=int(j)
    sum2=sum2+c
    count=count+1
    if count==(l//2):
        break
print("First Half Sum =",sum2)

for i in range (l//2):
    rem=a%10
    sum=rem+sum
    a=a//10
print("Second Half Sum =",sum)


if sum==sum2:
    print("Balanced Number")
else :
    print("Unbalanced Number")

