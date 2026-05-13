'''
21) Hollow Pyramid (Practice)
            *
           * *
          *   *
         *     *
        *********
'''

l=int(input("Enter number :"))

for i in range(l):
    print()
    for j in range (l-i):
        print(" ",end='')
    for k in range (i+1):
            if k==0 or i==l-1 :
                print("*",end='')
            else :
                print(" ",end='')
    for m in range (i):
            if  m==i-1 or i==l-1:
                print("*",end='')
            else :
                print(" ",end='')
    