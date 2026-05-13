'''
1. Smart Credit Card Approval System

A bank evaluates credit card applications based on income, credit score, employment type, and existing debt.

If income is greater than or equal to 50000, then check credit score. If credit score is greater than or equal to 750, then check debt. If debt is less than 20000, approve Premium Card; otherwise approve Gold Card. If credit score is less than 750, then check employment type. If employment is government and credit score is at least 650, approve Gold Card; otherwise reject.

If income is less than 50000, then check if income is at least 30000 and credit score is at least 700. If yes, approve Silver Card; otherwise reject.

Input:
Income = 45000
Credit Score = 720
Employment = private
Debt = 10000

Output:
Card Type = Silver Card
'''
a=int(input("Income ="))
b=int(input("Credit Score ="))
c=input("Employment =").lower()
d=int(input("Debt ="))

if a>=50000:
    if b>=750:
        if d<=20000:
            print("Card Type = Premium Card")
        else :
            print("Card Type = Gold Card")
    else :
        if c=='government' and b>=650:
            print("Card Type = Gold Card ")
        else :
            print("Rejected")
else:
    if a>=30000 and b>=700 :
        print("Card Type = Silver Card")
    else :
        print("Rejected")