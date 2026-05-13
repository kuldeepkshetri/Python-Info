'''Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
'''

s=int(input("Speed ="))
h,m=map(int,input("Time =").split())
a=m/60
b=h+a
d=s*b
print(f"Total Time ={b}hours")
print(f"Distance ={d} km")