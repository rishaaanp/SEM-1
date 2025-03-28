x=int(input("Enter the number"))
reverse=0
y=x
while x>0:
    reverse=reverse*10
    reverse=reverse+x%10
    x=x//10
print("Given number is",y)
print("Reverse of the number is",reverse)
if reverse==y:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
