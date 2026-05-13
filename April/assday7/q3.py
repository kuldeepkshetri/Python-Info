'''
3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000
'''
a=int(input("Enter annul income :"))

if a<=250000:
    print("No tax")
elif a<=500000 :
    c=a*5//100
    print("Tax Payable :",c)
elif a<=1000000 :
    c=a*20//100 
    print("Tax Payable :",c)
else :
    c=a*30//100
    print("Tax Payable :",c)
    