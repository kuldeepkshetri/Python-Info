'''Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
----------------------------------------
'''

dis ,time=map(int,input("Enter your distance and time :").split())

out=dis//time

print("Distance =",dis)
print("Time =",time)
print(f"Speed = {out} km/h" )

