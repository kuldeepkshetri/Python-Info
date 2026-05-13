'''2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction

Input:
Enter marks: 80

Output:
Pass
Distinction
'''

a=int(input("Enter marks :"))

if a>=40:
    print("Pass")
if a>=75:
    print("Distinction")