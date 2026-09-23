# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32     # Conversion formula
    return f


# Taking temperature input from user
celsius = float(input("Enter temperature in Celsius: "))

# Calling the function
fahrenheit = celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit:", fahrenheit)