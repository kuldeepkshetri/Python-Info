import random



print("--------------------Welcome To Escape Room--------------------")
print("Menu Of Game : \n1. Room 1  \n2. Room 2  \n3. Room 3  \n4. Room 4  \n5. Exit")
print("In each room you have to enter Direction from any of this \n.East \n.West \n.North \n.South ")

a=int(input("Enter Your Choice :"))
playing = True

while playing:

    match a : 
        case 1 :
            b=input("\nEnter First Direction :").lower()
            if "north"==b :
                c=input("\nEnter Second Direction :").lower()
                if "south"==c:
                    d=input("\nEnter Third Direction :").lower()
                    if "east"==d :
                        e=input("\nEnter Fourth Direction :").lower()
                        if "north"==e :
                            print("\n-------------------THE FINAL CHALLENGE-------------------")
                            print("There are 10 boxes. One contains the Golden Key.")
                            key=random.randint(1,10)
                            print("You have 3 Attempt")
                            rem=3
                            for i in range (1,4):
                                guess = int(input("Enter Your Box :"))
                                print("Attempt =",i)
                                if guess==key:
                                    print(f"CONGRATULATIONS! Box {guess} had the key! YOU WIN!")
                                    playing=False
                                    break
                                else :
                                    print("Wrong Guess ")
                                if i==3:
                                    print("Game Over Try Again :")
                                    print(f"{key} Box Contain the key")
                                    playing=False
                                    break    
                        else :
                            print("\nWrong Direction ")
                            
                    else :
                        print("\nWrong Direction ")
                        
                else :
                    print("\nWrong Direction")
                    
            else :
                print("\nWrong Direction ")
                        
        case 2 :
            b=input("\nEnter First Direction :").lower()
            if "east"==b :
                c=input("\nEnter Second Direction :").lower()
                if "east"==c:
                    d=input("\nEnter Third Direction :").lower()
                    if "east"==d :
                        e=input("\nEnter Fourth Direction :").lower()
                        if "east"==e :
                            print("\n-------------------THE FINAL CHALLENGE-------------------")
                            print("There are 10 boxes. One contains the Golden Key.")
                            key=random.randint(1,10)
                            print("You have 3 Attempt")
                            rem=3
                            for i in range (1,4):
                                guess = int(input("Enter Your Box :"))
                                print("Attempt =",i)
                                if guess==key:
                                    print(f"CONGRATULATIONS! Box {guess} had the key! YOU WIN!")
                                    playing=False
                                    break
                                else :
                                    print("Wrong Guess ")
                                if i==3:
                                    print("Game Over Try Again :")
                                    print(f"{key} Box Contain the key")
                                    playing=False
                                    break
                        else :
                            print("\nWrong Direction ")
                            
                    else :
                        print("\nWrong Direction ")
                        
                else :
                    print("\nWrong Direction")
                    
            else :
                print("\nWrong Direction ")
                       




        case 3 :
            b=input("\nEnter First Direction :").lower()
            if "east"==b :
                c=input("\nEnter Second Direction :").lower()
                if "west"==c:
                    d=input("\nEnter Third Direction :").lower()
                    if "north"==d :
                        e=input("\nEnter Fourth Direction :").lower()
                        if "south"==e :
                            print("\n-------------------THE FINAL CHALLENGE-------------------")
                            print("There are 10 boxes. One contains the Golden Key.")
                            print("You have 3 Attempt")
                            key=random.randint(1,10)
                            rem=3
                            for i in range (1,4):
                                guess = int(input("Enter Your Box :"))
                                print("Attempt =",i)
                                if guess==key:
                                    print(f"CONGRATULATIONS! Box {guess} had the key! YOU WIN!")
                                    playing=False
                                    break
                                else :
                                    print("Wrong Guess ")
                                if i==3:
                                    print("Game Over Try Again :")
                                    print(f"{key} Box Contain the key")
                                    playing=False
                                    break 
                        else :
                            print("\nWrong Direction ")
                            
                    else :
                        print("\nWrong Direction ")
                        
                else :
                    print("\nWrong Direction")
                    
            else :
                print("\nWrong Direction ")
                                               
                



        case 4 :
            b=input("\nEnter First Direction :").lower()
            if "south"==b :
                c=input("\nEnter Second Direction :").lower()
                if "north"==c:
                    d=input("\nEnter Third Direction :").lower()
                    if "west"==d :
                        e=input("\nEnter Fourth Direction :").lower()
                        if "east"==e :
                            print("\n-------------------THE FINAL CHALLENGE-------------------")
                            print("There are 10 boxes. One contains the Golden Key.")
                            print("You have 3 Attempt")
                            key=random.randint(1,10)
                            rem=3
                            for i in range (1,4):
                                guess = int(input("Enter Your Box :"))
                                print("Attempt =",i)
                                if guess==key:
                                    print(f"CONGRATULATIONS! Box {guess} had the key! YOU WIN!")
                                    playing=False
                                    break
                                else :
                                    print("Wrong Guess ")
                                if i==3:
                                    print("Game Over Try Again :")
                                    print(f"{key} Box Contain the key")
                                    playing=False
                                    break
                        else :
                            print("\nWrong Direction ")
                            
                    else :
                        print("\nWrong Direction ")
                        
                else :
                    print("\nWrong Direction")
                    
            else :
                print("\nWrong Direction ")
                                                    
        case 5 :
            print("\n----------------Quiting the Game----------------")
            break 
        case _ :
            print("\nInvalid Choice")
            playing =False
            