'''
4.
1. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected
'''

a=int(input("Input :"))
g=a
b=g%10
g=g//10
c=g%10
d=abs(b-c)
a=a//100
print("Initial Gap =",d)
while a>0:
    rem=a%10
    e=abs(c-rem)
    if e!=d:
        print("Pattern Break Detected")
        break
    a=a//10
    c=rem
else :
    print("Consistent Pattern")
