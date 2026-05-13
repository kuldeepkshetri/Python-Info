'''
25) Number Sandglass
    123454321
     1234321
      12321
       121
        1
       121
      12321
     1234321
    123454321
'''


l=int(input("Enter number :"))
h=1
for i in range (l):
    print()
    for j in range (i):
        print(" ",end='')
        h=1
    for k in range (l-i):
        print(h,end='')
        h=h+1
    for m in range (l-i-1,0,-1):
        print(m,end='')

g=1
for a in range (l-1,0,-1):
    print()
    g=1
    for b in range (a-1):
        print(" ",end='')
    for c in range (a-2,l-1):
        print(g,end="")
        g=g+1
        f=1
    for d in range (g+1,3,-1):
        print(d-3,end='')
        



