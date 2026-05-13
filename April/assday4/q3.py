'''
Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
'''

a,b,c,d,e=map(int,input("Marks =").split(","))
t=a+b+c+d+e
av=t/5
p=(t/500)*100
print("Total =",t)
print("Average =",av)
print("Percentage =",p)