# Create an empty list
numbers = []

# Ask the user how many integers they want to enter
n = int(input("How many integers do you want to enter? "))

# Take integers from the user one by one
for i in range(n):
    num = int(input("Enter an integer: "))
    numbers.append(num)

# Create an empty list to store the reversed list
reversed_list = []

# Start from the last element and move towards the first
for i in range(len(numbers) - 1, -1, -1):

 # Add each element to the reversed list
 reversed_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reversed_list)