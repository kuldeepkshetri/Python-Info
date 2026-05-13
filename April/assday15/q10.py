'''
10.
Electricity Bill Processing System (Multi-House)

An electricity board processes bills for multiple houses in a society.

Write a program to:

- Read number of houses n
- For each house:
    - Read units consumed
    - Calculate bill using slab rates:

        First 100 units      → ₹5 per unit  
        Next 100 units      → ₹7 per unit  
        Above 200 units     → ₹10 per unit  

    - Apply conditions:
        - If bill > ₹2000 → add 10% surcharge  
        - If units < 50 → give ₹100 subsidy  

    - Print bill for each house

- After processing all houses:
    - Print total bill collected
    - Print highest bill

---

Input:
3
120
250
40

Output:
House 1 Bill = 640
House 2 Bill = 1700
House 3 Bill = 100

Total Collection = 2440
Highest Bill = 1700
'''
a=int(input("Input :"))
i=1
sum=0
h=0

while i<=a:
    c=int(input("Input :"))
    if c<50 :
        bill=c*5-100
        print("House",i,"Bill",bill)
    else:
        if 100>=c:
            bill=c*5
            print(bill)
        elif 100<c<201:
            d=c-100
            bill=500+d*7
            print(bill)
        else :
            d=c-200
            bill=1200+d*10
            if bill>2000:
                cha=bill+(bill*0.1)
                print(cha)
            else:
                print(bill)
    i=i+1
    sum=sum+bill
    if h<bill:
        h=bill
print("Total Collection =",sum)
print("Highest Bill =",h)