x=int(input("Enter the number"))
i=1
k=0
while x==0:
    print("Every integer is a factor of 0")
else:
    while i<=x:
        if x%i==0:
            k=k+i
            i=i+1
        else:
            i=i+1  
    print("Sum of factors of",x,"is",k)
    
