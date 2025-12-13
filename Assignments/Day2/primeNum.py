    
num = int(input("enter number: "))

def isPrime(num):
    if num <= 1:
        print("it is not a prime number")
    else:
        i = 2
        while i <= num ** 0.5:
            if num % i == 0:
                print("it is not a prime number")
                break
            i += 1
        else:
            print("it is prime number")

prime=isPrime(num)