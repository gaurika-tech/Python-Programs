def factorial(n):
    result = 1

    # Multiply numbers from 1 to n
    for i in range(1, n + 1):
        result = result * i

    # Return the factorial value
    return result


# Take input from the user
n = int(input("Enter an integer: "))

# Call the factorial function and display the result
print("Factorial:", factorial(n))
