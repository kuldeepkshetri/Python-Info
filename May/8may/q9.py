'''
9.
    1
   10
  101
 1010
10101
'''

a=int(input("Enter no. :"))
ch=1
for i in range (a,1,-1):
    print()

    for j in range (1,i):
        print(" ",end='')
    for k in range (ch):
        if k%2==0:
            print("1",end='')
        else :
            print("0",end='')
    ch=ch+1