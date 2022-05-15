import math
p=float(input("Enter principle amount:"))
r=int(input("Enter rate of intrest(in %):"))

t=float(input("Time period (in months):"))
print("****INTRESTS****\n1.Compund(anually)\n2.Compound(halfyearly)\n3.Simple\n4.EXIT")
choice=int(input("Enter choice"))
while(choice!=4):    
    if(choice==1):
        n=t/12
        amount=p*(pow((1+r/100),n))
        print("The total amount compounded anually =",amount)
    elif(choice==2):
        n=t/6
        amount=p*(pow((1+r/200),n))
        print("The total amount compounded halfyearly =", amount)
    elif(choice==3):
        t=t/12               
        intrest=(p*r*t)/100
        amount=p+intrest
        print("The Simple intrest is",intrest)
        print("Total amount is",amount)
    choice=int(input("Enter choice:"))
        
        
        

        
