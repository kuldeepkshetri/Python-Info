'''
5)
A
AB
ABC
ABCD
ABCDE
'''

a=int(input("Enter the number :"))
for i in range (a):
    print()
    ch=65
    for j in range (i+1):
        print(chr(ch),end="")
        ch+=1