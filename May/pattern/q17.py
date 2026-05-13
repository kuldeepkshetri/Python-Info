'''
17) Hollow Hourglass
    * * * * * * *
      *       *  
        *   *   
          *       
        *   *    
      *       *   
    * * * * * * *
'''

l=int(input("Enter number :"))

for i in range (l):
    print()
    for j in range (l):
        if i==0 or i+1==l or i==j or i+1==l-j:
            print("* ",end='')
        else :
            print("  ",end='')