# Get string input from the user
user_string = input("\nEnter a string: ")
print(f"You entered: {user_string}")

# String length
string_length = len(user_string)
print(f"Length of the string: {string_length}")

# Convert string to uppercase
uppercase_string = user_string.upper()
print(f"Uppercase string: {uppercase_string}")

# Convert string to lowercase
lowercase_string = user_string.lower()
print(f"Lowercase string: {lowercase_string}")

# Replace a substring
old_substring = input("\nEnter a substring to replace: ")
new_substring = input("Enter the new substring: ")
user_string = user_string.replace(old_substring, new_substring)
print(f"String after replacement: {user_string}")

# Check if string contains a substring
substring = input("\nEnter a substring to check: ")
contains_substring = substring in user_string
print(f"Does the string contain '{substring}'? {contains_substring}")

# String concatenation
additional_string = input("\nEnter another string to concatenate: ")
concatenated_string = user_string + " " + additional_string
print(f"Concatenated string: {concatenated_string}")

# String slicing
start_index = int(input("\nEnter the start index for slicing: "))
end_index = int(input("Enter the end index for slicing: "))
sliced_string = user_string[start_index:end_index]
print(f"Sliced string: {sliced_string}")
