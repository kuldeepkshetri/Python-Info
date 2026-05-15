'''
1
23
456
78910

'''

'''
a=int(input("Enter number :"))
f=1
for i in range (a):
    print()
    for j in range (i+1):
        print(f,end='')
        f+=1
'''


'''
1
01
101
0101
10101
'''

'''
a=int(input("Enter number :"))
for i in range (1,a+1):
    print()
    for  j in range (1,i+1):
        if (i+j)%2==1 :
            print("0",end='')
        else :
            print("1",end='')
'''



'''
1
10
101
1010
10101
'''

'''
a=int(input("Enter number :"))
for i in range (1,a+1):
    print()
    for j in range (1,i+1):
        if j%2==1:
            print("1",end='')
        else :
            print("0",end='')
'''





'''
1
12
1 3
1  4
12345

'''

'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i+1):
        if j==0:
            print("1",end='')
        elif i==j or i+1==a:
            print(j+1,end='')
        else :
            print(" ",end='')
'''




'''
1
22
3 3
4  4
55555
'''



'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i+1):
        if  i==j:
            print(j+1,end='')
        elif i+1==a or j==0:
            print(i+1,end='')
        else :
            print(" ",end='')

'''









'''
5
54
543
5432
54321
'''


'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i+1):
        print(a-j,end='')
'''





'''
1
123
12345
1234567
123456789
'''


'''
a=int(input("Enter number :"))
for i in range (1,a+1):
    print()
    for j in range (1,i*2):
        print(j,end='')

'''









'''
1
10
1 1
1  0
10101
'''


'''
a=int(input("Enter number :"))
for i in range (a):
    print()
    for j in range (i+1):
        if j==0:
            print("1",end='')
        elif i+1==a or i==j:
            if j%2==0:
                print("1",end='')
            else :
                print("0",end='')
        else :
            print(" ",end='')

'''







'''
1
222
33333
4444444
555555555
'''


'''
a=int(input("Enter number :"))
for i in range (1,a+1):
    print()
    for j in range (1,i*2):
        print(i,end='')
'''









'''
12345
1234
123
12
1
'''

'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    for j in range (i):
        print(j+1,end='')
'''





'''
55555
4444
333
22
1
'''


'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    for j in range (i):
        print(i,end='')
'''





'''
123456
54321
1234
321
12
1
'''

'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    for j in range (i):
        if (a-i)%2==0:
            print(j+1,end='')
        else:
             print(i-j,end='')
'''







'''
54321
5432
543
54
5
'''


'''
a=int(input("Enter number :"))
for i in range (a,0,-1):
    print()
    k=i
    for j in range (i):
        print(k-j,end='')

'''










'''
55555
4  4
3 3
22
1
'''

'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    for j in range (i):
        if i==a or j==0 or j==i-1:
            print(i,end='')
        else:
            print(" ",end='')
'''



'''


55555
 4444
  333
   22
    1
'''

'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    for j in range (a):
        if j==a-1 or i==a or i>=a-j:
            print(i,end='')
        else :
            print(" ",end='')
'''


'''
12345
 1234
  123
   12
    1
'''


'''

a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    h=1
    for j in range (a):
        if i==a :
            print(j+1,end='')
        elif j==a-1:
            print(i,end='')
        elif i>=a-j:
            print(h,end='')
            h=h+1
        else :
            print(" ",end='')

'''



'''
12345
 1__4
  1_3
   12
    1
'''

'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    for j in range (a):
        if i==a :
            print(j+1,end='')
        elif j==a-1:
            print(i,end='')
        elif i==a-j:
            print("1",end='')
        elif i>a-j:
            print("_",end='')
        else :
            print(" ",end='')
'''



'''
55555
 4__4
  3_3
   22
    1
'''


'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    for j in range (a):
        if i==a :
            print(a,end='')
        elif j==a-1:
            print(i,end='')
        elif i==a-j:
            print(i,end='')
        elif i>a-j:
            print("_",end='')
        else :
            print(" ",end='')


'''







'''
11111
 2222
  333
   44
    5
'''

'''
a=int(input("Enter Number :"))
for i in range (a,0,-1):
    print()
    h=1
    for j in range (a):
        if i<a-j:
            print(" ",end='')
        else :
            print(a+1-i,end='')
'''


'''
    1
   12
  123
 1234
12345

'''

a=int(input("Enter number :"))
for i in range (a,0,-1)
