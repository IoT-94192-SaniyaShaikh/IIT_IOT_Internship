#Passing a Function to Another Function (Function as Argument)

def add(a,b):
    return a+b

def operator(func,x,y):
    return func(x,y)

print(operator(add,7,8))