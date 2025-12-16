#  Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
# Input: ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Output: [30.5, 34.25, 27.0, 23.25]

# Given tuple of tuples
data = ((10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4))

# Calculate averages
averages = []
num_tuples = len(data)

for i in range(len(data[0])):
    total = 0
    for t in data:
        total += t[i]
    averages.append(total / num_tuples)

print(averages)
