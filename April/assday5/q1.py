'''
1. Smart Voting & ID Verification System
   A government system verifies whether a citizen can vote and whether they have a valid ID.

* If age ≥ 18 → Eligible to vote
* If ID proof is available → Allowed inside booth

Input:
Enter age: 22
Do you have ID (yes/no): yes

Output:
Eligible to vote
Allowed inside booth

'''
a=int(input("Enter your age :"))
b=input("Do you have Id (yes/no) :")

if a >=18:
    print("Eligible to vote")

if b=='yes':
    print("Allowed inside booth")

if b=='no':
    print("Not Allowed inside booth")