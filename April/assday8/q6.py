'''
6. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged
'''

a=int(input("Transaction Amount ="))
b=input("Location =").lower()
c=int(input("Account Age ="))

if a>=10000:
    if b=='international':
        d=input("OTP :").lower()
        if d=='verified':
            print("Allowed")
        else :
            print("Blocked")
    elif b=='domestic':
        if a>=50000:
            if c>=2:
                print("Allowed")
            else :
                print("Flagged")
        else :
            print("Allowed")
else :
    e=input("Activity :").lower()
    if e=='unusual activity ':
        print("Flagged")
    else :
        print("Allowed")