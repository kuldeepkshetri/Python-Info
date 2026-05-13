'''

8) Border Number Pattern
    1 2 3 4 5
    2       5
    3       5
    4       5
    5 5 5 5 5

'''


l=int(input("Enter number :"))
for i in range (1,l+1):
    print()
    for j in range (1,l+1):
        if j==l or i==l:
            print(l,"",end='')
        elif j!=1 and j!=l and i!=1  :
            print("  ",end="")
        elif i==1:
            print(j,"",end="")
        else :
            print(i,"",end="")