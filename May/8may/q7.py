'''
7.
enter n6
     *
    **
   ***
  ****
 *****
******
'''

a=int(input("Enter no. :"))

for i in range (1,a+1):
    print()
    h=a-i
    for j in range (h,0,-1):
        print(" ",end="")
    for k in range (i):
        print("*",end="")