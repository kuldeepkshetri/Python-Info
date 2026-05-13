'''
2. Hospital Emergency Priority System

A hospital assigns treatment priority based on age, severity, and insurance.

If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.

If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.

If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

Input:
Age = 65
Severity = critical
Insurance = yes

Output:
Treatment = Immediate ICU
'''
a=int(input("Age ="))
b=input("Severity =").lower()
c=input("Insurance =")

if b=='critical':
    if a>=60:
        print("Treatment = Immediate ICU")
    else:
        print("Treatment =Emergency Ward")
elif b=='moderate':
    if c=='yes':
        print("Priority Treatment")
    else :
        print("General Queue")
else :
    if a<10:
        print("Pediatric Priority")
    else :
        print("Wait")