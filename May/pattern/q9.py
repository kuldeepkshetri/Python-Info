'''
9) Hollow Diamond Square
    **********
    ****  ****
    ***    ***
    **      **
    *        *
    *        *
    **      **
    ***    ***
    ****  ****
    **********
'''
l=int(input("Enter number"))

for i in range (l,0,-1):
    print()
    for j in range (i):
        print("*",end='')
    for k in range (l,i,-1):
        print("  ",end='')
    for m in range (i):
        print("*",end='')

for a in range (l,0,-1):
    print()
    for b in range (l+1,a,-1):
        print("*",end='')
    for c in range (1,a):
        print("  ",end='')
    for d in range (l+1,a,-1):
        print("*",end='')
   