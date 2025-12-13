num=int(input("Enter decimal number:"))

def binary(num):
    rem=0
    binary=0
    place=1
    while num>0 :
        rem= num%2
        binary=binary+rem*place
        num=num//2
        place*=10
    print(binary)

binary_number=binary(num)
