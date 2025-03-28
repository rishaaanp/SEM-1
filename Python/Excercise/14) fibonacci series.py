x=int(input("Enter the length of the fibonacci series"))
f1=0
f2=1
i=3
print(f1)
print(f2)
while i<=x:
    f3=f1+f2
    f1=f2
    f2=f3
    i=i+1
    print(f3)
