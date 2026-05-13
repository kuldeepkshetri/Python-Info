'''
4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit

---

Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!
'''

print("Menu Options:\n1 → Enter Units Consumed\n2 → Calculate Bill Amount\n* First 100 units → ₹5 per unit\n* Next 100 units → ₹7 per unit\n* Above 200 units → ₹10 per unit\n3 → Apply Surcharge\n* If bill > 2000 → 10% surcharge\n* Otherwise → 5% surcharge\4 → Display Final Bill5 → Exit")

a=None
while True :
    choice=int(input("Enter choice :"))
    match choice :
        case 1:
            a=int(input("Enter units consumed :"))
            print("Units recorded successfully")
        case 2 :
            if a==None :
                print("Please enter units consumed first")
            else :
                if a<101:
                    b=a*5
                elif 100<a<201:
                    b=(500+(a-100)*7)
                elif a>200 :
                    b=(1200+(a-200)*10)
                print("Bill Amount :",b)
        case 3 :
            if a==None :
                print("Please enter units consumed first")
            else :
                if b>2000:
                    c=int(b*0.01)
                else :
                    c=int(b*0.05)
                print("Surcharge :",c)
        case 4 :
            if a==None :
                print("Please enter units consumed first")
            else :
                print("----- Final Bill -----")
                print("Units :",a)
                print("Bill Amount :",b)
                print("Surcharge :",c)
                print("Total PAyable :",(b+c))
        case 5 :
            if a==None :
                print("Please enter units consumed first")
            else :
                print("Exiting system.... Thank you!")
                break 
        case _:
            print("Invalid choice . please try again.") 
                        

