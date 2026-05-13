'''
**9. Check All Digits Are Even**
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to **check whether all digits of a number are even using loops**.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
'''
a=int(input("Input ="))
b=len(str(a))
count=0
s=a


print("From while loop")
while a>0 :
    rem=a%10
    if rem%2==0:
       count+=1
    a=a//10
if count==b:
    print("All Even")
else :
    print("Not All Even")


print("-----------------------------------------------------------")

print("From for loop")
c=0
for i in range (b):
    rem=s%10
    if rem%2==0:
        c=c+1
    s=s//10
if c==b:
    print("All Even")
else :
    print("Not All Even")    