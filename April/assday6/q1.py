'''
1. A bank wants to automate its loan approval process. The system should take salary, 
credit score, and number of existing loans as input. If the salary is greater than or equal to 30000, 
then it should check the credit score. If the credit score is greater than or equal to 750,
 the loan should be approved. Otherwise, it should check the number of existing loans. 
If the existing loans are less than 2, the loan should be conditionally approved; otherwise, it should be rejected. 
If the salary is less than 30000, the loan should be rejected. Display the final loan status.

Input:
Salary = 40000
Credit Score = 720
Existing Loans = 1

Output:
Loan Status = Conditional Approval
'''

a=int(input("Salary ="))
b=int(input("Credit Score ="))
c=int(input("Existing Loans ="))

if a>=30000:
    if b>=750:
        print("Loan Approved")
    else :
        if c<2:
            print("Conditional Approval")
        else :
            print("Rejected")
else :
    print("Rejected")
