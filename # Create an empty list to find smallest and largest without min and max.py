# Create an empty list
numbers = []

# Take 7 integers 
for i in range(7):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# Let the first number is the smallest
smallest = numbers[0]

# Let the first number is the largest
largest = numbers[0]

for num in numbers:

    # Check if the number is smaller
    if num < smallest:
        smallest = num

    # Check if the number is larger
    if num > largest:
        largest = num

print("Smallest:", smallest)
print("Largest:", largest)