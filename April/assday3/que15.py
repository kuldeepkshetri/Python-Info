'''Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h'''


a=int(input("Distance1 ="))
b=int(input("Time1 ="))
c=int(input("Distance2 ="))
d=int(input("Time2 ="))

s1=a/b
s2=c/d
t=(s1+s2)/2

print(f"Average Speed ={t}km/h")


