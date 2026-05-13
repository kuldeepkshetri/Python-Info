'''
8.
enter n6
 654321
  65432
   6543
    654
     65
'''

a=int(input("Enter no. :"))



i=1
while i<a:
    print()
    j=a
    k=0
    while k<i:
        print(" ",end='')
        k=k+1


    while j>=i:
        print(j,end="")
        j=j-1
    i=i+1
