'''
4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
'''
a=input("Subscription = ").lower()
b=int(input("Progress = "))
c=int(input("Test Score = "))

if a=='premium':
    if b>79:
        if c>69:
            print("Unlock Certificate")
        else :
            print("Retry") 
    else :
        print("Complete Course")
elif a=='basic':
    if b>49:
        print("Limited Access")
    else :
        print("Lock Content ")
else :
    print("Deny")