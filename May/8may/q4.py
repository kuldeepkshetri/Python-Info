'''
4)
1
00
111
0000
11111
'''

a=int(input("Enter the number :"))
for i in range(1,a+1):
    print()
    for j in range (1,i+1):
        if i%2==0:
            print("0",end="")
        else :
            print("1",end="")