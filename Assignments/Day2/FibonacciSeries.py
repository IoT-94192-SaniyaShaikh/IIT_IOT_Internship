num=int(input("enter number for fibonacci count:"))
i=0
a,b=0,1
for i in range(num) :
    print(a," ")
    a,b=b,a+b
