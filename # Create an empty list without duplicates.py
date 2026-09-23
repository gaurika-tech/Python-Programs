# Create an empty list
numbers = []

# how many numbers to enter
n = int(input("How many integers do you want to enter? "))

# Take integers from the user one by one
for i in range(n):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# Create an empty list for unique numbers
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique)