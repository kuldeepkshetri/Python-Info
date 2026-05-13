a = input("Input : ")
print("Repeated Digits =", end=" ")

seen = ""

for i in a:
    if i not in seen:
        count = 0

        for j in a:
            if i == j:
                count += 1

        if count > 1:
            print(i, end=" ")

        
        
