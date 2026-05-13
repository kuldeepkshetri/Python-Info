'''
22) Inverted Hollow Pyramid
    *********
     *     *
      *   *
       * *
        *
'''


l=int(input("Enter number :"))

for i in range(l):
    print()
    for j in range (i):
        print(" ",end='')
    for k in range (i,l):
        if i==0 or k==i:
            print("*",end='')
        else :
            print(" ",end='')
    for m in range (i,l-1):
        if i==0 or m==l-2:
            print("*",end='')
        else :
            print(" ",end='')
    
 
        