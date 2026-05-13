'''
**11. Count Occurrence of a Digit**
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to **count how many times a given digit appears in a number using loops**.

Input: Number = 122312, Digit = 2
Output: 3
'''




i=int(input("input :"))
d=int(input("Digit :"))
count=0

v=i



while i>0:
    tem=i%10
    if d==tem:
        count+=1
    i=i//10
print("From while loop")
print("Output :",count)

print("--------------------------------------------------------")

le=len(str(v))
c=0

for j in range(v):
    rem=v%10
    if d==rem :
        c=c+1
    v=v//10
print("From for loop")
print("Output :",c)    
