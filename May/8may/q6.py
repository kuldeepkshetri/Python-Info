'''
6)
a
ab
abc
abcd
abcde
'''


a=int(input("Enter the number :"))
for i in range (a):
    print()
    ch=97
    for j in range (i+1):
        print(chr(ch),end="")
        ch+=1