x=int(input("Enter the 4 digit number"))
a=x//100  
b=x%100   
c=a//10   
d=a%10    
e=b//10   
f=b%10   
product=(c*e)-(d*f)
sum=c+d+e+f
print(sum)
reverse=0
while x>0:
    reverse=reverse*10
    reverse=reverse+x%10
    x=x//10
print(reverse)
print(product)
