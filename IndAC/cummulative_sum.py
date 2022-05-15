a=[]
n=int(input("Enter number of elements:"))
for x in range(n):
    element=int(input("Enter element:"))
    a.append(element)
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print("The original list is:",a)
print("Cummulative sum is",b)
