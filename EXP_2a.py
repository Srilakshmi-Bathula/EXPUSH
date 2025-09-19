# Take two integer inputs from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform relational operations
print(f"\nRelational Operations between {num1} and {num2}:")
print(f"{num1} > {num2}  is {num1 > num2}")
print(f"{num1} < {num2}  is {num1 < num2}")
print(f"{num1} == {num2}  is {num1 == num2}")
print(f"{num1} != {num2}  is {num1 != num2}")
print(f"{num1} >= {num2}  is {num1 >= num2}")
print(f"{num1} <= {num2}  is {num1 <= num2}")

# Perform logical operations
print(f"\nLogical Operations between {num1} and {num2}:")
is_positive1 = num1 > 0
is_positive2 = num2 > 0

print(f"Both numbers are positive: {is_positive1 and is_positive2}")
print(f"At least one number is positive: {is_positive1 or is_positive2}")
print(f"First number is not positive: {not is_positive1}")
print(f"Second number is not positive: {not is_positive2}")

# Combining relational and logical operations
print(f"\nCombining Relational and Logical Operations:")
X = (is_positive1 or is_positive2) and (num1 != num2)
print(f"At least one number is positive and both are not equal: {X}")
