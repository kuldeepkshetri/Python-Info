'''
23) Plus Star Pattern
        *
        *
    *********
        *
        *
'''



for i in range (1,6):
    print()
    for j in range (1,6):
        if i==3 :
            print("*",end='')
        elif j!=5:
            print(" ",end='')
        else :
            print("*",end='')
    for k in range (1,5):
        if i==3:
            print("*",end='')