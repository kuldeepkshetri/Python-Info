'''
24) Hollow X Pattern
    *   *
     * *
      *
     * *
    *   *
'''




l=int(input("Enter number :"))

for i in range (l):
    print()
    for j in range (l):
        if i==j or i+1==l-j :
            print("*",end='')
        else :
            print(" ",end='' )
    