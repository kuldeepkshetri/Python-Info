'''Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0
'''

a=int(input("Mobile price ="))
b=int(input("Down payment ="))
c=int(input("Interest ="))
d=int(input("Months ="))

e=a-b
f=e+(e*10/100)
m=f/d
print("Remaining Amount =",e)
print("Total With Interest =",f)
print("Monthly EMI =",m)