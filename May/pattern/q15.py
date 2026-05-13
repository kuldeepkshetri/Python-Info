'''
15) Zig-Zag Star
    *   *   *
      *   *
    *   *   *
'''
l=int(input("Enter number :"))

for i in range (1,l+1):
    print()
    for j in range (1,(l*2)):
        if i%2==1 and j%2==1:
            print("* ",end='')
        elif i%2==0 and j%2==0:
            print("* ",end='')
        else :
            print("  ",end='')