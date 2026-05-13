'''
6) Number Triangle with Dashes
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9

'''


l=int(input("Enter number :"))


for i in range (1,l+1):
    print()
    g=i
    for j in range (l,i,-1):
        print("- ",end='')
    for k in range (i):
        print(g,"",end='')
        g=g+1