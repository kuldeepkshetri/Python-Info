'''
4.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number
'''
a=input("Input :")
c=int(a[0])
count=0
max=0

print("Differences :",end=" ")
for i in a:
    d=int(i)
    if d!=c :
        dif=abs(c-d)
        c=d
        print(dif,end=" ")
        if dif>2:
            count=count+1
        if max<dif:
            max=dif
print("\nMax Difference =",max)
if count==0:
    print("Smooth Number ")
else :
    print("Irregular Number")