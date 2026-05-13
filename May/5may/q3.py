'''
3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if.
'''
a=int(input("Years of experience is :"))
b=int(input("Salary :"))

print("Salary : ", b+(0.3*b) if a>=10 else b+(0.2*b) if a>=5 else b+(0.1*b))
