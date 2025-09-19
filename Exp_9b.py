def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci(limit):
    i = 0
    while True:
        fib_number = fibonacci(i)
        if fib_number > limit:
            break
        print(fib_number, end=" ")
        i += 1
    print()

# Main part of the program
while True:
    input_value = input("Enter the maximum value for the Fibonacci sequence (or type 'exit' to quit): ")

    if input_value.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    try:
        limit = int(input_value)
        if limit >= 0:
            print(f"Fibonacci sequence up to {limit}:")
            print_fibonacci(limit)
            print()
        else:
            print("Please enter a non-negative integer.\n")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer or type 'exit' to quit.\n")
