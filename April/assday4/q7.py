'''
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
'''


a=int(input("Total runs ="))
b=float(input("Overs ="))
c=int(b)
d=(b-c)*10
e=6*c+d
print("Total balls =",e)
f=(a/e)*6
print("Run Rate =",round(f,2))
