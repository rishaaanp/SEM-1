name=input("Enter the name of the employee:")
code=int(input("Enter the code of the employee:"))
BP=int(input("Enter the basic pay:"))
print("")

if BP<10000:
    DA=(5/100)*BP
    HRA=(2.5/100)*BP
    MA=500
    PT=20
    PF=(8/100)*BP
    IT=(0/100)*BP
    
elif BP<30000:
    DA=(7.5/100)*BP
    HRA=(5/100)*BP
    MA=2500
    PT=60
    PF=(8/100)*BP
    IT=(0/100)*BP
    
elif BP<50000:
    DA=(11/100)*BP
    HRA=(7.5/100)*BP
    MA=5000
    PT=60
    PF=(11/100)*BP
    IT=(11/100)*BP
else:
    DA=(25/100)*BP
    HRA=(11/100)*BP
    MA=7000
    PT=80
    PF=(12/100)*BP
    IT=(20/100)*BP

def GrossSalary(a,b,c,d):
    grossSalary=a+b+c+d
    print("The gross salary is:",grossSalary)
    return grossSalary

def Deduction(e,f,g):
    deduction=e+f+g
    print("The deducted amount is:",deduction)
    return deduction

def NetSalary(i,j):
    netSalary=i-j
    print("The net salary is:",netSalary)
    return netSalary

GS=GrossSalary(BP,DA,HRA,MA)
D=Deduction(PT,PF,IT)
NetSalary(GS,D)
