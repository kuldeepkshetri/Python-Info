'''
7.
 Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime'''

a=input("Input : ")
num=0
sum=0

for i in a:
    num=num+1
    if num%2==0 :
        continue
    sum=sum+int(i)
print(sum)


for i in range (2,sum//2+1):
    if sum%i==0:
        print("Not Prime")
        break
else :
    print("Prime ")


    
