x=int(input("Enter the first digit"))
y=int(input("Enter the second digit"))
if x<10 and y<10:
    print("Two digit number is",x,y)
    if x<y:
        print(x,"is smaller than",y)
    else:
        print(y,"is smaller than",x)
else:
    print("It is not a two digit number")
