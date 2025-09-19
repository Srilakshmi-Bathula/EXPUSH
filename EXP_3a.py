# Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
exponentiation = num1 ** num2
floor_division = num1 // num2

# Display the results
print(f"\nArithmetic Operations between {num1} and {num2}:")
print(f"Sum: {num1} + {num2} = {sum}")
print(f"Difference: {num1} - {num2} = {difference}")
print(f"Product: {num1} * {num2} = {product}")
print(f"Quotient: {num1} / {num2} = {quotient}")
print(f"Remainder: {num1} % {num2} = {remainder}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")
print(f"Floor Division: {num1} // {num2} = {floor_division}")
