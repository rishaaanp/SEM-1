x=int(input("Enter number of days"))
a=x//365
b=(x%365)//30
c=(x%365)%7
print(a,"Years",b,"Months",c,"Days")
