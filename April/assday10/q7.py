'''
**7. Count Even Digits**
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to **count the number of even digits in a given number using loops**.

Input: 123456
Output: Even digits count = 3
'''

a=int(input("Input ="))
count=0
len=len(str(a))
b=a

while a>0:
    rem=a%10
    if rem%2==0 :
        count+=1
    a=a//10
print("Even digits count =",count)

even=0
for i in range (len):
    rem=b%10
    if rem%2==0 :
        even=even+1
    b=b//10
print("Even digits count =",even)