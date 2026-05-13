'''
11) Butterfly Number Pattern
    1      1
    12    21
    123  321
    12344321
    123  321
    12    21
    1      1
'''



l=4

for i in range (l,0,-1):
    print()
    m=1
    for j in range (l,i-1,-1):
        print(m,end='')
        m=m+1
    for k in range ((i-1)*2):
        print(" ",end='')
    for g in range (i-1,0,-1):
        print("k",end='')