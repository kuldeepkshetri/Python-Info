'''
***** 
**** 
***
**
* 
'''
'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    for j in range (i):
        print("*",end='')
'''




'''
*****
####
***
##
*
'''
'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    for j in range (i):
        if i%2==0:
            print("#",end='')
        else :
            print("*",end='')
'''


'''
*
##
***
####
*****


'''

'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i+1):
        if i%2==0:
            print("*",end='')
        else :
            print("#",end='')

'''


'''
*
* *
*   *
*     *
* * * * *
'''

'''
a=int(input("Enter Number :"))
for i in range (a):
    print()
    for j in range (i+1):
        if j==0 or i==j or i==a-1:
            print(" *",end='')
        else :
            print("  ",end='')
'''








'''
*
**
*@*
*@@*
* * * * *


'''


'''
a=int(input("Enter Number :"))
for i in range (a):
    print()
    for j in range (i+1):
        if j==0 or i==j or i==a-1:
            print("* ",end='')
        else :
            print("@ ",end='')

'''



'''
*
*#
*#*
*#*#
*#*#*


'''

'''
a=int(input("Enter Number :"))
for i in range (a):
    print()
    for j in range (i+1):
        if j%2==0:
            print("*",end='')
        else :
            print("#",end='')

'''





'''

*****
*  *
* *
**
*
'''

'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    for j in range (i):
        if j==0 or i==a or i==j+1:
            print("*",end='')
        else :
            print(" ",end='')

'''