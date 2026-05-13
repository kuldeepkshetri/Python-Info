'''
3. Perfect Number Reward System

A gaming company rewards users if entered number is a Perfect Number.

(Perfect Number = sum of proper factors equals number)

Write a program using for-else loop to:

- Find sum of proper factors
- If sum equals number print Reward Unlocked
- Else print Try Again

Input:
6

Output:
Reward Unlocked
'''
a=int(input("Input ="))
fact=0

for i in range (1,a//2+1):
    if a%i==0:
        fact=fact+i
if a==fact:
    print("Reward Unlocked")
else :
    print("No Reward")