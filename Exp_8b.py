def multiplication_table(start, end):
    i = start
    while i <= end:
        print(f"Multiplication table for {i}:")
        j = 1
        while j <= 10:
            print(f"{i} x {j} = {i * j}")
            j += 1
        print()
        i += 1

# Main part of the program
start_value = input("Enter a number to start the multiplication table from: ")
end_value = input("Enter a number to end the multiplication table until: ")

try:
    start_num = int(start_value)
    if start_num <= 0:
        print("Starting number must be greater than 0.")
    else:
        try:
            end_num = int(end_value)
            if start_num <= end_num:
                multiplication_table(start_num, end_num)
            else:
                print("Ending number must be greater than or equal to the starting number.")
        except ValueError:
            print("Invalid input for ending number. Please enter a valid number.")
except ValueError:
    print("Invalid input for starting number. Please enter a valid number.")
