a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a>b:
    while b!=0:
        r=a%b
        a=b
        b=r
    else:
        if a>0:
            print("GCD=",a)
        else:
            a=-(a)
            print("GCD=",a)
else:
    while a!=0:
        r=b%a
        b=a
        a=r
    else:
        if b>0:
            print("GCD=",b)
        else:
            b=-(b)
            print("GCD=",b)
        
