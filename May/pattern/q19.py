'''
19) Reverse Number Cross
    5   5
     4 4
      3
     4 4
    5   5
'''
l=int(input("Enter number :"))

for i in range (l):
    print()
    for j in range (l):
        if i==j and i<3:
            print(l-j,end='')
        elif i==j and i>2:
            print(j+1,end='')
        elif i+1==l-j and j>2:
            print(j+1,end='')
        elif i+1==l-j and j<3:
            print(i+1,end='')
        else :
            print(" ",end='')
