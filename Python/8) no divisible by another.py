x=int(input("Enter the number to be divided"))
y=int(input("Enter the divisor"))
z=x/y
if x%y==0:
    print(x,"is divisible by",y)
    print("Quotient is",z)
else:
    print(x,"is not divisible by",y)
