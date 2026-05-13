import random 


print("----------------------- Math Practice Program -----------------------")
print("It Contain :\n5 Easy \n7 Medium \n8 Hard questions \nGood luck!")


total=20
correct=0


for i in range (1,total+1):
    if i<=5:
        level="Easy"
        s=1
        e=20
    elif i<=12 :
        level="Medium"
        s=20
        e=50
    else :
        level="Hard"
        s=50
        e=100
    


    op=random.choice("+-*/")
    num1=random.randint(s , e)
    num2=random.randint(s , e)


    if op=="+":
        ans=num1+num2
    elif op=="*":
        ans=num1*num2
    elif op=="-":
        if num1<num2 :
            num1,num2=num2,num1
        ans=num1-num2
    elif op=="/":
        s=num1*num2
        ans=num1
        num1=s
        




    print(f"{level} level : \nQ{i}. {num1}{op}{num2}")

    user=int(input("Enter Your Answer :"))


    if user==ans:
        print("Correct Answer !")
        correct+=1
    else :
        print("Wrong Answer ")



    
 
print("-------------------------QUIZ FINISHED-------------------------")
print(f"Score: {correct}/{total}")

per=(correct/total)*100
print("Percentage :",per,"%")



if correct==20:
    print("Excellent !!!!!!")
elif correct>15:
    print("Close Enough")
elif correct>10:
    print("Nice Try")
else :
    print("Practice Needed")
 

    

        



