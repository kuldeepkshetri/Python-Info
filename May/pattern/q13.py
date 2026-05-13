'''
13) Number X Pattern
    1   5
     2 4
      3
     2 4
    1   5
'''


l=int(input("Enter number :"))
for i in range (l):
    print()
    for j in range (l):
        if i==j:
            print(i+1,end='')
        elif i+1==l-j:
            print(j+1,end='')
            
        else :
            print(" ",end='')