x=int(input("Enter the number"))
y=len(str(x))
sqr=x**2
last=sqr%pow(10,y)
if last==x:
    print(x,"is an automorphic no")
else:
    print(x,"is not an automorphic no")
