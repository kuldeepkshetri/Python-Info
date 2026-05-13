'''
27) Continuous Number Pyramid
            1
           2 3
          4 5 6
         7 8 9 10
'''
l=int(input("Enter number :"))
c=1
for i in range (l):
    print()
    for j in range (i,l):
        print(" ",end='')
    for k in range (i+1):
        print(c,"",end='')
        c=c+1