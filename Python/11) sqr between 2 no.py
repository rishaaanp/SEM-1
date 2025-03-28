x=int(input("Enter first number"))
y=int(input("Enter second number"))
count=y-x
count1=x-y
b=1
c=1
if x>y:
    while c<count1:          
        y=y+1               
        a=y*y               
        print(a)            
        c=c+1
else:
    while b<count:          
        x=x+1               
        a=x*x               
        print(a)            
        b=b+1
