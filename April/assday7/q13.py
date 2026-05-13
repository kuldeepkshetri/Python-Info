'''
13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600
'''

a=int(input("Enter Salary :"))
b=int(input("Enter Rating :"))


if b==5:
    if a<20001 :
        c=a*0.25+a+2000
        print("Revised Salary :",c)
    else :
        c=a*0.25+a
        print("Revised Salary :",c)
elif b==4:
     if a<20001 :
        c=a*0.20+a+2000
        print("Revised Salary :",c)
     else:
        c=a*0.20+a
        print("Revised Salary :",c)
elif b==3:
    c=a*0.10+a
    print("Revised Salary :",c)
elif b==2:
    c=a*0.05+a 
    print("Revised Salary :",c)
else:
    print("No Hike")



