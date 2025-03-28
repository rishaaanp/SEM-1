x=int(input("Enter the number"))
reverse=0
y=x
while x>0:
    reverse=reverse*10
    reverse=reverse+x%10
    x=x//10
print("Given number is",y)
print("Reverse of the number is",reverse)
