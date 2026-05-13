'''
20) Continuous Diamond Numbers
           1
          2 3
         4 5 6
        7 8 9 10
         4 5 6
          2 3
           1

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

for a in range (l-1):
    print()
    c=c-(2*(l-a)-1)
    for b in range (a+2):
        print(" ",end='')
    for d in range (l-1,a,-1):
        print(c,"",end='')
        c=c+1
