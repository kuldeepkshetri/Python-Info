'''
2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
'''

a=int(input("Input :"))
sum=0
pro=1
digit=0

while a>0:
    rem=a%10
    sum=sum+rem
    pro=pro*rem
    a=a//10
print("Sum =",sum)
print("Product =",pro)


d=abs(sum-pro)
di=d
print("Difference =",d)
while d>0:
    d=d//10
    digit=digit+1
print("Digit =",digit)

f=di+digit
print("Final Result =",f)


for i in range (2,f//2+1):
    if f%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
