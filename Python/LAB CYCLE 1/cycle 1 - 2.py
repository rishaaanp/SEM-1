def read():
    i=int(input("Enter first side of the triangle:"))
    j=int(input("Enter second side of the triangle:"))
    k=int(input("Enter third side of the triangle:"))
    return i,j,k

a,b,c=read()
print("")
d,e,f=read()
print("")

def area(x,y,z):
    s=(x+y+z)/2
    area=(s*(s-x)*(s-y)*(s-z))**1/2
    print("Area of the triangle is:",area)
    return area

area1=area(a,b,c)
area2=area(d,e,f)
totalarea=area1+area2
area1percent=(area1/totalarea)*100
area2percent=(area2/totalarea)*100

print("The percentage composition of the first triangle is:",area1percent)
print("The percentage composition of the second triangle is:",area2percent)
