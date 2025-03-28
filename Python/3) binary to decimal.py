b=int(input("Enter the binary number"))
d=0
q=b
i=0
while q!=0:
    digit=q%10
    q=q//10
    d=d+digit*2**i
    i=i+1
print("Given binary number is",b)
print("Equivalent decimal number is",d)
