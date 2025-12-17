from operation import arithmetic,string_ops

a=int(input("enter the number1:"))
b=int(input("enter the number2:"))

print("Addition of two numbers:",arithmetic.add(a,b))
print("multiplication of two numbers:",arithmetic.multiply(a,b))

s1=input("enter the string:")

print("reversed string:",string_ops.reverse(s1))
print("count of vowels:",string_ops.count_vow(s1))