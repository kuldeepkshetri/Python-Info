'''
2)	WAP to print Square, Cube and Square Root of all numbers from 1 to N
'''


a=int(input("Enter Number :"))
sum=0

for i in range (1,a+1):
    b=i**2
    c=i**3
    d=i**0.5
    sum=b+c+d+sum
print(sum)



 