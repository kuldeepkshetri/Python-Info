'''
2. University Result Processing System
A university wants to automatically assign grades based on marks.
Marks ≥90 → A+
Marks ≥75 → A
Marks ≥60 → B
Marks ≥50 → C
Below 50 → Fail
Write a program using a single nested inline if expression to display the grade.
'''

a=int(input("Input :"))

print("Marks → ","A+" if a>=90 else "A" if a>=75 else "B" if a>=60 else "C" if a>=50 else "C" if a>=50 else "Fail" )
