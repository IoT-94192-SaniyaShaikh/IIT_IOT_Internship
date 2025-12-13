num=int(input("enter the 5 digit number:"))

original=num
rev=0
while num>0 :
    digit=num%10
    rev=rev*10+digit
    num=num//10

if original==rev:
    print("it is a palindrome")
else :
    print("the number is not palindrome")

