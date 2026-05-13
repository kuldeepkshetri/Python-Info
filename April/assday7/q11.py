'''
A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600
'''

a=int(input("Enter distance :"))
b= input("Enter class :")

if a<=100:
    if b=='AC':
        print("Total Fare : ₹200")
    elif b=='Sleeper':
        print("Total Fare : ₹100")
elif 100<a<501:
    if b=='AC':
        print("Total Fare : ₹600")
    elif b=='Sleeper':
        print("Total Fare : ₹300")
else:
    if b=='AC':
        print("Total Fare : ₹200")
    elif b=='Sleeper':
        print("Total Fare : ₹100")