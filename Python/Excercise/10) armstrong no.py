num=int(input("Enter the number"))
num1=num
k=0
i=0
while num1!=0:
    a=num1%10
    num1=num1//10
    i=i+1
else:
    num1=num
    while num1!=0:
        a=num1%10
        num1=num1//10
        k=k+(a**i)
    else:
        if k==num:
            print(num,"is an armstrong no")
        else:
            print(num,"is not an armstrong no")
