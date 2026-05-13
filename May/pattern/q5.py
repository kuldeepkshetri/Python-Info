'''
5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1******1
'''


i=int(input("Enter number :"))
g=i

while i>1:
    print()
    j=1

    while j<i:
        print(j,end='')
        j=j+1
    for k in range (g,i,-1):
        
        print("**",end='')
    for m in range (i-1,0,-1):
        print(m,end='')

    i=i-1    
           