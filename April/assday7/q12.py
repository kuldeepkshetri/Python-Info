'''

12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680
'''
a=float(input("Enter bill amount :"))

if a<1001:
    b=a*0.05+a
    print("Final Bill Amount :",int(b))
elif 1000<a<5001:
    b=a*0.12+a
    if a>3000:
        print("Final Bill Amount :",int(b+200))
    else :
        print("Final Bill Amount :",int(b))
else :
    b=a*0.18+a
    print("Final Bill Amount :",int(b))