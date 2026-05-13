a=int(input("Unit1="))
b=int(input("Unit2="))
c=int(input("Unit3="))
d=int(input("Unit4="))
e=int(input("Unit5="))
f=int(input("Unit6="))

if a>b and a>c and a>d and a>e and a>f :
    print("Highest Stack =",a)
if a<b and b>c and b>d and b>e and b>f :
    print(b)
if c>b and a<c and c>d and c>e and c>f :
    print(c)
if d>b and d>c and a<d and d>e and d>f :
    print(d)
if e>b and e>c and e>d and a<e and e>f :
    print(e)
if f>a and f>b and f>c and f>d and f>e :
    print(f)