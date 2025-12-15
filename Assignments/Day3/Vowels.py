# 3. Write a function to count number of vowels in a given string. Write another function to count the
# number of consonants. Write one more function to calculate the ratio of number of vowels to number
# of consonants in given string. Input a string from user and print the ratio

# Input string
s1 = input("Enter the string: ").lower()

# Function to count vowels
def count_vowels(s):
    return (s.count('a') + s.count('e') +
            s.count('i') + s.count('o') +
            s.count('u'))

# Function to count consonants
def count_consonants(s):
    letters = sum(1 for ch in s if ch.isalpha())
    vowels = count_vowels(s)
    return letters - vowels

# Function to calculate ratio
def vowel_consonant_ratio(s):
    v = count_vowels(s)
    c = count_consonants(s)
    if c == 0:
        return "Undefined (no consonants)"
    return v / c

# Function calls
vowel_count = count_vowels(s1)
consonant_count = count_consonants(s1)
ratio = vowel_consonant_ratio(s1)

# Output
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Vowel to Consonant Ratio:", ratio)

    