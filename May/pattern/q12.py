'''
12) Hollow Diamond Numbers
       1
      2 2
     3   3
    4     4
     3   3
      2 2
       1
'''

l=int(input("Enter number"))

for i in range (1,l+1):
    print()
    b=i
    for j in range (l,i,-1):
        print(" ",end='')
    for k in range (1,i+1):
        if k==1:
            print(b,end='')
            
        else :
            print(" ",end='')
    for m in range (1,i):
        if m==i-1:
            print(b,end='')
        else :
            print(" ",end='')





g=l-1


for a in range (g,0,-1):
    print()
    for b in range (l-a):
        print(" ",end='')
    for c in range (1,a+1):
        if c==1:
            print(a,end='')
        else :
            print(" ",end='')
    for d in range (1,a):
        if d==a-1:
            print(a,end='')
        else :
            print(" ",end='')








