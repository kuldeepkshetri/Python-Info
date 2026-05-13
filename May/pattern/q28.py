'''
28) Hollow Square
    *****
    *   *
    *   *
    *   *
    *****
'''
l=int(input("Enter number :"))
for i in range (l):
    print()
    for j in range (l):
        if i==0 or i==l-1:
            print("*",end='') 
        else :
            if  j==0 or j==l-1:
                print("*",end='')
            else :
                print(" ",end='')
