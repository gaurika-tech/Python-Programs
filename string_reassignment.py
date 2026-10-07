# Function to change the first character of the string
def change_string(s):
    s = "X" + s[1:]     # Creates a new string with first character as X
    print("Inside function:", s)


# Taking string input from user
s = input("Enter a string: ")

print("Before function:", s)

# Calling the function
change_string(s)

# Checking the original string
print("After function:", s)