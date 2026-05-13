'''
1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.
'''

a=int(input("Input :"))
b=input("Customer Type :").lower()

if b=="premium":
    print("Total amount= ",a-(0.2*a) if b=="premium" and a>5000 else a-(a*0.1) )
else :
    print("Total amount =",a-(0.1*a)if b=="regular" and a>3000 else (a-0.05*a) )
