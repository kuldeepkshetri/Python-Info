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






'''
    *
   * *
  * * *
 * * * *
* * * * *


'''


'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (1,a-i):
        print(" ",end='')
    for k in range (i+1):
        print("*",end=' ' )
'''



'''

    *
   ***
  *****
 *******
*********
'''
'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (1,a-i):
        print(" ",end='')
    for k in range (i*2+1):
        print("*",end='' )
'''





'''
    *
   *_*
  *___* 
 *_____* 
*********
'''
'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (1,a-i):
        print(" ",end='')
    for k in range (i*2+1):
        if k==0 or i+1==a or k==i*2:
            print("*",end='' )
        else :
            print("_",end='')
'''





'''
*********
 ******* 
  ***** 
   ***
    * 


'''


'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    for k in range (a-i):
        print(" ",end='')
    for j in range (i*2-1):
        print("*",end='')
'''




'''

    #
   *#* 
  **#** 
 ***#*** 
****#****
'''

'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (1,a-i):
        print(" ",end='')
    for k in range (i*2+1):
        if k==i:
            print("#",end='')
        else :
            print("*",end='' )
'''




'''


* * * * * 
 * * * * 
  * * * 
   * * 
    *
'''

'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i):
        print(" ",end='')
    for k in range (a-i):
        print("*",end=' ')
'''


'''


   *
  ***
 ***** 
******* 
 ***** 
  *** 
   *
'''
'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (a-i):
        print(" ",end='')
    for k in range (i*2+1):
        print("*",end='')
for c in range (a-1,0,-1):
    print()
    for b in range (a-c+1):
        print(" ",end='')
    for d in range (c*2-1):
        print("*",end='')
'''






'''
x
xx
xxx
xxxx
xxx
xx
x

'''

'''
a = int(input("Enter number: "))

for i in range(a * 2 - 1):
    print()
    if i < a:
        g= i + 1 
    else:
        g= (a * 2 - 1) - i  
        
    for j in range(g):
        print("x", end='')

'''











'''
    X 
   X_X 
  X___X
 X_____X
X X X X X
'''

'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (a-i-1):
        print(" ",end='')
    for k in range (i*2+1):
        if k==0 or k==i*2 :
            print("x",end='')
        elif i+1==a:
            print("x",end='')
        else :
            print("_",end='')
'''














'''
*        *
**      **
***    ***
****  ****
**********
'''

'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i+1):
        print("*",end='')
    for k in range ((a-1-i)*2):
        print(" ",end='')
    for m in range (i+1):
        print("*",end='')
'''








'''


**********
****  ****
***    ***
**      **
*        *
'''



'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (a-i):
        print("*",end='')
    for k in range (i*2):
        print(" ",end='')
    for m in range (a-i):
        print("*",end='')
'''












'''
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



'''

a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (a-i):
        print("*",end='')
    for k in range (i*2):
        print(" ",end='')
    for m in range (a-i):
        print("*",end='')



for b in range (a):
    print()
    for c in range (b+1):
        print("*",end='')
    for d in range ((a-1-b)*2):
        print(" ",end='')
    for e in range (b+1):
        print("*",end='')

'''





'''


*     *
 *   *
  * *
   *
  * *
 *   *
*     *
'''

'''
a=int(input("Enter number :"))
for i in range (a*2-1):
    print()
    for j in range (a*2-1):
        if i==j or  i+j==a*2-2 :
            print("*",end='')
        else :
            print(" ",end='')

'''









'''

\     /
 \   /
  \ /
   \
  / \
 /   \
/     \ 

'''






'''

a=int(input("Enter number :"))
f="\\"
for i in range (a*2-1):
    print()
    for j in range (a*2-1):
        if i==j  :
            print(f,end='')
        elif   i+j==a*2-2 :
            print("/",end='')
        else :
            print(" ",end='')

'''









'''
   *
  *_*
 *_*_*
*_*_*_*
 *_*_*
  *_*
   *  
'''




'''
a=int(input("Enter number "))
for i in range (a):
    print()
    for j in range (a-i-1):
        print(" ",end='')
    for k in range (i*2+1):
        if k%2==0:
            print("*",end='')
        else :
            print("_",end='')

for b in range (1,a):
    print()
    for c in range (b):
        print(" ",end='')
    for d in range ((a-1-b)*2+1):
        if d%2==0:
            print("*",end='')
        else :
            print("_",end='')
'''