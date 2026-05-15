'''
    1
    2
    3
    4
123454321
    4
    3
    2
    1
'''

'''
l=int(input("Enter Number :"))
for i in range (1,l+1):
    print()
    for j in range (1,l+1):
        if i==l:
            print(j,end='')
        elif j==l:
            print(i,end='')
        else :
            print(" ",end='')
    for k in range (1,l):
        if i==l:
            print(l-k,end='')
for a in range (1,l+1):
    print()
    for b in range (0,l):
        if b+1==l and l-a!=0:
            print(l-a,end='')
        else :
            print(" ",end='')
        
'''            


'''
1
12
123
1234
123
12
1
'''
'''
l=int(input("Enter number :"))

for i in range (1,l+1):
    print()
    
    for j in range (1,i+1):
        print(j,end='')
for a in range (l-1,0,-1):
    print()
    for b in range (1,a+1):
        print(b,end='')
'''

'''


123456789
 1+++++7
  1+++5
   1+3
    1	
'''
'''
l=int(input("Enter number :"))
for i in range (1,l+1):
    print()
    for j in range (1,l*2):
        if i==1 :
            print(j,end="")
        elif i==j:
            print("1",end='')
        elif l*2-i==j:
            print(j-i+1,end='')
        elif i<j and j<l*2-i:
            print("+",end='')
        else :
            print(" ",end="")
'''


'''
123456789
 1     7
  1   5
   1 3
    1
'''
'''
l=int(input("Enter number :"))
for i in range (1,l+1):
    print()
    for j in range (1,l*2):
        if i==1 :
            print(j,end="")
        elif i==j:
            print("1",end='')
        elif l*2-i==j:
            print(j-i+1,end='')
        else :
            print(" ",end="")
'''


'''


123456789
 1234567
  12345
   123
    1

'''

'''
l=int(input("Enter number :"))
for i in range (1,l+1):
    print()
    m=2
    for j in range (1,l*2):
        if i==1 :
            print(j,end="")
        elif i==j:
            print("1",end='')
        elif l*2-i==j:
            print(j-i+1,end='')
        elif i<j and j<l*2-i:
            print(m,end='')
            m=m+1
        else :
            print(" ",end="")

'''

'''
    1
   1*1
  1***1
 1*****1
111111111
'''

l=5
for i in range (1,l+1):
    print()
    for j in range (1,l*2):
        if i==l:
            print("1",end="")
        else :
            print(" ",end='')