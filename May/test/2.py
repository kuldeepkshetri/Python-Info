n=int(input("Enter the Number ="))
threshold=int(input("Enter the thresold ="))
sum=0
count=0
l=len(str(n))
print("Digit processed :")
for i in range(l):
    digit=n%10
    n//=10
    sum+=digit
    count+=1
    print(digit,end=" ")

   # l2=len(str(sum))
    #for i in range(l2):
    if sum>threshold:
            print()
            print("Sum =",sum)
            print("Count =",count)
            print("Threshold Exceeded")
            break
else:
    print()
    print("Sum =",sum)
    print("Count =",count)
    print("Threshold Not Reached")