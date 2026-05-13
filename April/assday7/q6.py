'''

6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000
'''
a=int(input("Enter Salary :"))
b=int(input("Enter years of experience :"))

if b>10:
    print("Bous Amount : ₹",int(a*0.2))
elif 5<b<=10 :
    print("Bonus Amount : ₹",int(a*0.1))
elif 2<b<=5 :
    print("Bonus Amount : ₹",int(a*0.05))
else :
    print("No bonus")