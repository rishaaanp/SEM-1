x=int(input("Enter the length of the series"))
count=0
a=0
sum=0
while a<x:
    count=count+1
    b=count*count
    sum=sum+b
    print(b)
    a=a+1
print("Total sum is",sum)
