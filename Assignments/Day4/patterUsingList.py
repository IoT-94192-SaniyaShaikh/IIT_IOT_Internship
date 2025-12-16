#  Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For
# example, histogram([4, 9, 7]) should print the following

def histogram(value):
    for number in value:
        print("*"*number)

numbers=list(map(int,input("enter the list").split()))

histogram(numbers)



