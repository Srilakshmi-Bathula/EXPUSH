# Input from the user
num_str = input("Enter a number: ")

print("\nData Type Conversion:")
# Convert string to integer
num_int = int(num_str)
print(f"String to Integer: {num_str} -> {num_int}")

# Convert string to float
num_float = float(num_str)
print(f"String to Float: {num_str} -> {num_float}")

# Convert integer to float
int_to_float = float(num_int)
print(f"Integer to Float: {num_int} -> {int_to_float}")

# Convert float to integer
float_to_int = int(num_float)
print(f"Float to Integer: {num_float} -> {float_to_int}")

# Convert integer to string
int_to_str = str(num_int)
print(f"Integer to String: {num_int} -> {int_to_str}")

# Convert float to string
float_to_str = str(num_float)
print(f"Float to String: {num_float} -> {float_to_str}")

# Convert integer to boolean (0 is False, any other number is True)
int_to_bool = bool(num_int)
print(f"Integer to Boolean: {num_int} -> {int_to_bool}")

# Convert string to boolean (empty string is False, any other string is True)
str_to_bool = bool(num_str)
print(f"String to Boolean: '{num_str}' -> {str_to_bool}")
