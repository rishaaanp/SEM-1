a=int(input("Enter your 'a' value"))
b=int(input("Enter your 'b' value"))
c=int(input("Enter your 'c' value"))
d=(b*b)-(4*a*c)
if d>0:
    print("d=",d,",equation has real and distinct roots")
elif d==0:
    print("d=",d,",equation has real and equal roots")
else:
    print("d=",d,",equation has no real roots")

