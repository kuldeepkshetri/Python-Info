'''
4.Electricity Billing System
An electricity board calculates bills based on units consumed:
Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit
Write a program to compute total bill using inline if.
'''

a=int(input("Unit :"))

print("Bill is =",(a*5) if a<=100 else (500+(a-100)*7) if 101<=a<=300 else (1900+(a-300)*10))



