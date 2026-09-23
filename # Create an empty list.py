# Create an empty list
numbers = []

# Take 10 integers from the user
for i in range(10):
    n = int(input("Enter an integer: "))
    numbers.append(n)

# Create a variable to store the sum
total = 0

# Add each number to total
for n in numbers:
    total = total + n
    
average = total / 10

print("Sum:", total)
print("Average:", average)