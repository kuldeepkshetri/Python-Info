'''
3.
Digit Neighbor Sum Analyzer

A system analyzes the relationship between a digit and its immediate neighbors.

Write a program to:

Traverse digits from left to right (ignore first and last digit)
For each digit, calculate sum of its adjacent digits
Check if current digit is equal to the sum of its neighbors                                                         
Display such digits
Count how many such digits exist
If none found → print No Matching Digit
Else → print Neighbor Sum Pattern Found

Input:
121314

Output:
Matching Digits: 2 3
Count = 2
Neighbor Sum Pattern Found
'''

n=int(input("Enter a number: "))
c=0
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
m=rev
print("Match Digits:",end=" ")
while m>0:
    rem=m%10
    m=m//10
    rem1=m%10
    j=m//10
    j=j%10
    sum=rem+rem1
    if j==sum:
        print(rem,end=" ")
        c=c+1
print("\nCount =",c)
if c==0:
    print("No matching Digit")
else:
    print("Neighbour Sum Pattern Found")