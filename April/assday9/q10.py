'''
10. Military Recruitment Fitness System
Selection is based on age, BMI, running time, and medical condition.

If age is between 18 and 25, then check BMI. If BMI is between 18 and 25, then check running time. If running time is less than or equal to 15 minutes, then check medical. If medical is fit, select; otherwise medical reject. If running time is more than 15, physical fail. If BMI is not in range, BMI fail.

If age is between 26 and 30, then check running time and medical. If running time is less than or equal to 14 and medical is fit, conditional selection; otherwise reject.

If age is above 30 or below 18, not eligible.

Input:
Age = 23
BMI = 22
Running Time = 14
Medical = fit

Output:
Selection Status = Selected
'''

a=int(input("Age ="))
b=int(input("BMI ="))
c=int(input("Running Time ="))
d=input("Medical =").lower()

if 18<a<25:
    if 18<b<25:
        if c<=15:
            if d=='fit':
                print("Selection Status = Selected")
            else :
                print("Selection Status = Rejected")
        else: 
            print("Selection Status = Physical Fail")
    else :
        print("Selection Status = BMI Fail")   
elif 26<a<30:
    if c<=14 and d=='fit':
        print("Selection Status = Conditional Selection")
    else :
        print("Selection Status = Rejected")
else :
    print("Not Eligible")