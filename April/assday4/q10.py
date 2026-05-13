'''Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4

'''

a=int(input("Total seconds ="))
b=a//3600
c=(a%3600)
d=c//60
e=c%60
print("Hours =",b)
print("Minutes =",d)
print("Seconds =",e)