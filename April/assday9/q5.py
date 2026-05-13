'''
5. Smart Exam Evaluation System

A student’s result depends on marks, attendance, and internal score.

If marks are 40 or above, then check attendance. If attendance is 75 or above, then check internal marks. If internal is 20 or above, result is Pass; otherwise Grace Pass. If attendance is below 75, result is Detained.

If marks are below 40, then check if marks are at least 35 and internal is at least 25. If yes, result is Reappear; otherwise Fail.

Input:
Marks = 38
Attendance = 80
Internal = 26

Output:
Result = Reappear
'''

a=int(input("Marks ="))
b=int(input("Attendance ="))
c=int(input("Internal ="))

if a>=40:
    if b>=75:
        if c>=20:
            print("Result = Pass")
        else :
            print("Result = Grace Pass")
    print("Detained")
else :
    if a>=35 and c>=25:
        print("Result = Reappear")
    else :
        print("Result = Fail")