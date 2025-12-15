#Explore default parameter values of function, Keyword Arguments (You can send #arguments with the
#key = value syntax) and how we can pass function to the another function.

#Default Parameter Values in Functions
def greet(name, msg="Hello"):
    print(msg, name)

greet("Alice")              # Uses default value
greet("Bob", "Good Morning")

def name(name, surname="Shaikh"):
    print(name,surname)
name("saniya")