x=int(input("Enter the number of seconds"))
a=x//3600
b=(x%3600)//60
c=(x%3600)%60
print(a,"Hours",b,"Minutes",c,"Seconds")
