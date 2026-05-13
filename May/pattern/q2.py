'''
2) Hollow Rectangle
    *********
    *       *
    *       *
    *       *
    *********
'''


l=int(input("Enter number :"))

for i in range (l):
    print()
    for j in range (l):
        if i==0 or i==l-1 or j==0 :
            print("*",end="")
        else :
            print(" ",end='')
    for k in range (l-1):
        if i==0 or i==l-1 :
            print("*",end='')
        elif k==l-2:
            print("*",end='')
        else :
            print(" ",end='')