'''
29) Diagonal Number Square
    1 - - -
    - 2 - -
    - - 3 -
    - - - 4
'''


l=int(input("Enter number :"))

for i in range (1,l+1):
    print()
    for j in range (1,l+1):
        if i==j:
            print(i,"",end='')
        else :
            print("- ",end='')