def print_factors(num):
    print(f"Factors of {num} are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

number = int(input("Enter a number: "))
print_factors(number)
