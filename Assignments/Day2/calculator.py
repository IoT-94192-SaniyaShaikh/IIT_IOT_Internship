num1=int(input("enter number: "))
num2=int(input("enter number: "))

while 1:
    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")

    choice=int(input("enter your choice: "))

    match choice:
        case 1:
            print("addition of number is: ",num1+num2)
    
        case 2:
             print("Subtraction of number is: ",num1-num2)

        case 3:
            print("Multiplication of number is: ",num1*num2)

        case 4:
            print("Division of number is:",num1/num2)

        case _:
             print("invalid operation")
             break