'''
1. Sum of First N Natural Numbers
A teacher wants to reward students by giving points daily. On day 1, a student gets 1 point, day 2 → 2 points, and so on. This follows a natural number sequence.
Write a program to calculate the **total points earned after n days** by summing all natural numbers up to n using loops.

Input: n = 10
Output: Total Points = 55
'''

n=int(input("Enter number :"))
a=0
for i in range (1,n+1):
    a=a+i
print("Total Points =",a)

sum=0
x=1
while x<=n:
    sum=sum+x
    x+=1
print("Total Points =",sum)