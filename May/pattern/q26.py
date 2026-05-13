'''
26) Right Hollow Number Triangle
    1
    12
    1 3
    1  4
    12345
'''

l=int(input("Enter n :"))


for i in range (1,l+1):
    print()
    for j in range (1,i+1):
        if j==1 or j==i or i==l:
            print(j,end='')
        else :
            print(" ",end='')