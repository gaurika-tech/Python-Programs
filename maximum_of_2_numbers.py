def find_maximum (num1 , num2):
    if num1 > num2:
       return num1
    else :
       return num2

# Ask the user to input the values
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

#Call the function and find the maximum
maximum = find_maximum(first_number, second_number)

print(f"The greater number is: {maximum}")
   