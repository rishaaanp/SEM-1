x=int(input("Enter first number"))
y=int(input("Enter second number"))
z=int(input("Enter third number"))
if x<y and x<z:
    print(x,"is the smallest")
elif y<x and y<z:
    print(y,"is the smallest")
else:
    print(z,"is the smallest")
