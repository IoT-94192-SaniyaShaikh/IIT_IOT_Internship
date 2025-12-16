# Define a function overlapping() that takes two lists and returns True if they have at least one member in
# common, False otherwise.

def overlapping():
    l1=list(map(int,input("Enter elements separated by space: ").split()))
    l2=list(map(int,input("enter second list elements seperated by space: ").split()))
    print("List1",l1)
    print("List2:",l2)

    for element in l1:
        if element in l2:
            print("true")
            break
        print("false")
        
overlapping()