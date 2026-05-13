'''
10) Slanted Star Block
    ****
     ****
      ****
       ****
'''
l=int(input("Enter number :"))


for i in range (l):
    print()
    for j in range (i):
        print(" ",end='')
    for k in range(l-1):
        print("*",end='')