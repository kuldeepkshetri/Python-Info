'''
16) Palindrome Pyramid
            1
           121
          12321
         1234321
        123454321
'''

l=5

for i in range (1,l+1):
    print()
    for j in range (l,i,-1):
        print("m",end='')
    for k in range (1,i+1):
        print(k,end="")
    for m in range (i-1,0,-1):
        print(m,end='')