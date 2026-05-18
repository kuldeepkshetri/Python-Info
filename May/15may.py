







'''
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
'''


'''
a=input("Enter message :").lower()
v=0
for i in a :
    if i in "aeiou":
        v=v+1
print("Total Vowels :",v)
'''












'''
2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5
'''


'''
a=input("Enter message :")
s=0
for i in a :
    if i==" ":
        s=s+1
print("Total Spaces :",s)
'''









'''
3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times
'''


'''
a=input("Enter Review :").
b=input("Enter character :")
c=0

for i in a:
    if i==b:
        c=c+1
print(f"Character '{b}' occurs: {c} times")
'''











'''
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11
'''



'''
a=input("Enter name :").lower()
c=0

for i in a:
    if i not in "aeiou" and i!=" ":
        c=c+1
print("Total Consonants :",c)

'''









'''



5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password
'''



"""
password=input("Enter your password : ")
upper1=0
upper2=0
lower=0
digit=0
special=0
space=0
if len(password)>=8 and len(password)<=15:
    
    
    if password[0]>="A" and password[0]<="Z":
        upper1=1
    if password[-1]>="1" and password<="9":
        digit=1
    for ch in password:
        if ch>="a" and ch<="z":
            lower=1
        elif ch>="A" and ch<="Z":
            upper2=1
        elif ch>="1" and ch<="9":
            digit+=1
        elif ch==" ":
            space=1
        else:
            special=1
    
else:
    print("Password must be contain at lest 8 character")
if upper1==1 and digit>=2 and space==0 and special==1 and lower==1 and upper2>=0:
    print("valid Password")
else:
    print("not valid password") 
"""










"""
6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number
"""




"""
pnr=input("Enter your PNR num : ").upper()
chart=0
digit=0
cha=0
special=0
if len(pnr)>=12:
    if pnr[0]=="P" and pnr[1]=="N" and pnr[2]=="R":
        chart=1
    for i in pnr:
        if i>="1" and i<="9":
            digit+=1
        if i>="A" and i<="Z":
            cha=1
        else:
            special=1
else:
    print("PNR must be more then 12 character")
if chart==1 and digit==9 and cha==1 and special==0:
    print("PNR number is valid")
else:
    print("Invalid PNR number")
"""











"""
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
"""












"""
num=input("Enter your vehicle registration num : ").upper()
ch=0
char=0
digit=0
di=0
special=0
if len(num)==10:
    if num[0]>="A" and num[0]<="Z" and num[1]>="A" and num[1]<="Z":
        ch=1
    if num[2]>="0" and num[2]<="9" and num[3]>="0" and num[3]<="9":
        digit=1

    for i in num:
        if i>="0" and i<="9":
            di=1
        elif i>="A" and i<="Z":
            char=1
        else:
            special=1
else:
    print("registration num should be 10 charter")
if ch==1 and digit==1 and di>=0 and char>=0 and special==0:
    print("valid register num")
    print(num)
else:
    print("Invalid")
"""