'''

14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
'''

a=input("Enter course category :").lower()
b=input("Enter user type :").lower()

if a=='programming':
    if b=='student':
        print("Final Course Fee: ₹4000")
    elif b=='working professional':
        print("Final Course Fee: ₹4500")
    else :
        print("Final Course Fee: ₹5000")
elif a=='design':
    if b=="student":
        print("Final Course Fee: ₹3200")
    elif b=='working professional':
        print("Final Course Fee: ₹3600")
    else :
        print("Final Course Fee: ₹4000")
elif a=='marketing':
    if b=="student":
        print("Final Course Fee: ₹2400")
    elif b=='working professional':
        print("Final Course Fee: ₹2700")
    else :
        print("Final Course Fee: ₹3000")