'''
5. Smart Warehouse Dispatch System

A warehouse decides dispatch strategy based on stock availability, priority level, and delivery distance.

If stock is at least 100, then check priority. If high priority, then check distance. If distance is up to 200, dispatch immediately; otherwise use fast courier. If priority is not high, then check if stock is at least 300. If yes, bulk dispatch; otherwise normal dispatch. If stock is less than 100, then check if stock is at least 50. If yes, and priority is high, partially dispatch; otherwise hold. If stock is below 50, mark out of stock.

Input:
Stock = 120
Priority = high
Distance = 300

Output:
Dispatch Status = Dispatch via Fast Courier
'''

a=int(input("Stock ="))
b=input("Priority =").lower()
c=int(input("Distance ="))

if a>=100:
    if b=='high':
        if c<=200:
            print("Dispatch Immediately")
        else:
            print("Fast Courier")
    else :
        if a>=300:
            print("Bulk Dispatch")
        else :
            print("Normal Dispatch")
else :
    if a>=50:
        if b=='high':
            print("Partially Dispatch")
        else :
            print("Hold")
    else :
        print("Out of Stock") 