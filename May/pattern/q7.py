'''
7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5

'''

l=int(input("Enter number :"))

for i in range (1,l+1):
    print()
    m=i*2-2
    for j in range (1,i):
        print(m,"",end='')
        m=m-1
    for k in range (l,i,-1):
        print("- ",end='')