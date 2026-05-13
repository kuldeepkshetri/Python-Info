'''

1) Hollow Pyramid
        *
       * *
      *   *
     *     *
    *********

'''


l=int(input("Enter number :"))

for i in range (1,l+1):
    print()
    for j in range (i,l):
        print(" ",end='')
    for k in range (i):
        if i==l or k==0:
            print("*",end='')
        else :
            print(" ",end='')
    for m in range (1,i):
        if i==l or m==i-1:
            print("*",end='')
        else :
            print(" ",end='')