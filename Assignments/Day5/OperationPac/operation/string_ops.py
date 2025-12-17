# string_ops.py should contain functions to reverse a string and count vowels.
def reverse(s):
    return s[::-1]

def count_vow(s):
    vowels="aeiouAEIOU"
    count=0
    for ch in s:
        if ch in vowels:
            count+=1
    return count