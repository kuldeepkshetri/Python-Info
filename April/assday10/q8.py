'''
**8. Count Odd Digits**
A banking system flags IDs with too many odd digits for further verification.
Write a program to **count the number of odd digits in a given number using loops**.

Input: 123456
Output: Odd digits count = 3
'''

a=int(input("Input ="))
count=0
len=len(str(a))
b=a

while a>0:
    rem=a%10
    if rem%2!=0 :
        count+=1
    a=a//10
print("Odd digits count =",count)



odd=0
for i in range (len):
    rem=b%10
    if rem%2!=0 :
        odd=odd+1
    b=b//10
print("Odd digits count =",odd)