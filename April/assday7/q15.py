'''
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220
'''

a=input("Enter vehicle type: ").lower()
b=int(input("Enter hours parked :"))


if a=='bike':
    c=b*10
    if b>5:
        print("Total Parking Fee :",c+100)
    else :
        print("Total Parking Fee :",c)
elif a=='car':
    c=b*20
    if b>5:
        print("Total Parking Fee :",c+100)
    else :
        print("Total Parking Fee :",c)
elif a=='bus':
    c=b*50
    if b>5:
        print("Total Parking Fee :",c+100)
    else :
        print("Total Parking Fee :",c)

