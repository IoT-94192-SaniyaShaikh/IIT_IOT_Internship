#Write different functions to perform basic arithmetic operations. Write another function with name
#calculate which takes three arguments as operand1, operand2 and function to perfrom operation and
#returns the result of operation. Test above function for different set of inputs.

num1=int(input("enter number: "))
num2=int(input("enter number: "))

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
   return num1/num2

def calculator(func,num1,num2):
    return func(num1,num2)

while 1:
    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")

    choice=int(input("enter choice:"))

    if choice==1:
        print("Sum of two number is:",calculator(add,num1,num2))
        

    elif choice==2:
        print("subtraction of two number is:",calculator(sub,num1,num2))

    elif choice==3:
        print("multiplication of number is:",calculator(mul,num1,num2))

    elif choice==4 :
         print("Division of two number is:",calculator(div,num1,num2))
    else:
        print("wrong choice")
        break



    

