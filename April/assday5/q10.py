'''
10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
Pass
Eligible for certificate
'''

a=int(input("Enter marks :"))
b=int(input("Enter attendance :"))

if a>=40:
    print("Pass")
if b>=75:
    print("Eligible for certificate")