'''
========================================
Assignment 3: Split the Bill
========================================

You and your friends went out to eat. The bill was quite high and you want to split it evenly.

Write a Python program that:
- Accepts the total bill amount.
- Accepts the number of friends.
- Displays how much each person should pay.

Example:
Total bill = 1250
Friends = 5
Each should pay = 250.0
'''

Amount=int(input("Enter the total bill amount:"))
Friend=int(input("Enter the number of friends:"))

print(f"Total bill = {Amount} \nFriends = {Friend}")

pay=Amount/Friend
print("Each should pay =",pay)


