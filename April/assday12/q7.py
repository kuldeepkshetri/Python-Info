'''7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number
'''
b=input("Input : ")
rev=0
a=int(b)
print(b)
count=0
 
for i in b:
    if 0==int(i):
        print("Rejecetd")
        break
    else:
        while a>0:
            rem=a%10
            if rem==0:
                count=count+1
            a=a//10
        if count>=1:
            print("Duck Number")
            break
        else :
            print("Not Duck Number")
            break



    