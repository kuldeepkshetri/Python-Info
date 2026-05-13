'''
**12. Multiplication of Digits**
A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
Write a program to **find the product of all digits of a number using loops and then check whether the result is even or odd**.

Input: 1234
Output: 24
Even
'''

i=int(input("Input ="))
out=1
v=i
c=len(str(v))


print("From while loop")
while i>0:
    rem=i%10
    out=out*rem
    i=i//10
print("Output",out)
if out%2==0:
    print("Even")
else :
    print("Odd")


print("---------------------------------------")

print("From for loop")
o=1
for j in range(c):
    rem=v%10
    o=o*rem
    v=v//10
print("Output",o)
    
if o%2==0:
    print("Even")
else :
    print("Odd")