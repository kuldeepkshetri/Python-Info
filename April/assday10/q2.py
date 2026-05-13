'''
2. Factorial of a Number
In project scheduling, tasks are dependent on previous tasks, and the total number of ways to arrange them is calculated using factorial. Factorial of a number n is the product of all numbers from 1 to n.
Write a program to calculate the **factorial of a given number using loops**.

Input: n = 5
Output: Total Ways = 120
'''
n=int(input("n="))
fact=1


for i in range (1,n+1):
    fact=fact*i
print("Total Ways =",fact)

b=1
c=1


while b<=n:
    c=c*b
    b+=1
print("Total Ways =",fact)