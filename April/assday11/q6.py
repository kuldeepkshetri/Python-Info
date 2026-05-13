'''
6. Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12
'''

a=int(input("Input :"))
count=0
for i in range (1,a+1):
    s=a%i
    if s==0:
        count=count+i
print("Factors Count = ",count)